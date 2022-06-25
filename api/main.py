from requests.auth import HTTPBasicAuth
from datetime import date
import requests

# Train Data SOurced from Real Train TImes API
username = "rttapi_mpvii"
password = "f63e45c3ffd06e42cd5d77f5b371be72497172fb"

# url = "https://api.rtt.io/api/v1/json/search/MDL/to/HAZ"

# Get Today's dat in YYYY/MM/DD
# today = date.today().strftime("%Y/%m/%d")
today = "2022/06/24/0815"

endpoint = "https://api.rtt.io/api/v1"

call = f"/json/search/MDL/to/MAN/{today}"



response = requests.get(endpoint+call, auth=HTTPBasicAuth(username, password))
journeys = response.json()['services']

for journey in journeys:
    print(journey['locationDetail']['realtimeDeparture'])



call2 = f"/json/search/HAZ/to/MAN/{today}"
response2 = requests.get(endpoint+call2, auth=HTTPBasicAuth(username, password))
print(response2.content)



