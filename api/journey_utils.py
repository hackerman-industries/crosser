"""Module to handle train journeys from realtraintimes api"""
from datetime import date
import logging
import time
import requests
from requests.auth import HTTPBasicAuth
from model.journey import Journey
from model.crossing import Crossing

# Train data sourced from RealTrainTimes API
USER = "rttapi_mpvii"
PASS = "f63e45c3ffd06e42cd5d77f5b371be72497172fb"
ENDPOINT = "https://api.rtt.io/api/v1"
FORMAT = "json"

# Get today's date in YYYY/MM/DD
DATE = date.today().strftime("%Y/%m/%d")

# Set our use-case services that impact a crossing
SERVICES = [
    ["DSL", "HAZ"],
    ["HAZ", "DSL"],
    ["HAZ", "MDL"],
    ["MDL", "HAZ"]
]

# Log level set for testing
logging.basicConfig(level=logging.DEBUG)

def get_journeys(start_pos, end_pos, journey_date=DATE):
    """
    Returns information on train journeys from one station to another for a given day.

    Args:
        start_pos (str): Code of the station where the journey begins.
        end_pos (str): Code of the station where the journey ends.
        journey_date (str): The required date to check for journeys. In format YYYY/MM/DD.

    Returns:
        list: A list of journey objects.
    """
    logging.info(f"Getting journeys for {start_pos}-{end_pos}")

    outbound_data = requests.get(
        f"{ENDPOINT}/{FORMAT}/search/{start_pos}/to/{end_pos}/{journey_date}",
        auth=HTTPBasicAuth(USER, PASS)
    ).json()['services']

    # Sleeping for any weird shit on the api end
    time.sleep(1)

    arrival_data = requests.get(
        f"{ENDPOINT}/{FORMAT}/search/{end_pos}/from/{start_pos}/{journey_date}",
        auth=HTTPBasicAuth(USER, PASS)
    ).json()['services']

    # Clean arrival data
    # Data in the past is very scuffed for whatever reason
    # Needs investigating, sometimes the 'arrival_data' will show services
    # that are not from the correct station.
    # Other times the arrival/outbound data will be completely off.
    # This is recorded around a day of train strikes, so not sure how much impact that's had.
    # Or it could be that actual times are being updated for one station, and not another

    # This step cleans some of those situations up, but it needs to be figured out.
    logging.info("Cleaning arrival data")
    service_ids = []

    for service in outbound_data:
        service_ids.append(service['serviceUid'])

    arrival_data = [item for item in arrival_data if item['serviceUid'] in service_ids]

    journeys = []

    # Parse API data into a reusable object
    for i in range(len(outbound_data)):
        journeys.append(Journey(
            start_pos,
            end_pos,
            journey_date,
            int(outbound_data[i]['locationDetail']['realtimeDeparture']),
            int(arrival_data[i]['locationDetail']['realtimeArrival'])
        ))

    return journeys


def get_all_journeys(services=SERVICES, journey_date=DATE):
    """
    Returns information on train journeys between stations to another for a given day.

    Args:
        services (list): A list of services to get journeys for.
        journey_date (str): The required date to check for journeys. In format YYYY/MM/DD.

    Returns:
        list: A list of journey objects.
    """
    logging.info(f"Getting all journeys for {services}")
    journeys = []

    for service in services:
        journeys.extend(get_journeys(service[0], service[1], journey_date))

    return journeys
