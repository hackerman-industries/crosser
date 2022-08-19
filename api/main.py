from model.crossing import Crossing
from model.journey import Journey
from journey_utils import get_all_journeys, SERVICES, DATE

def get_crossing_events(time):
    """
    """
    crossing = Crossing("HAZ", 4, 2, 3)

    journeys = get_all_journeys(SERVICES, DATE)

    for journey in journeys:
        crossing_times = crossing.calculate_journey_crossing_time(journey)
        
        if crossing_times[0] <= time <= crossing_times[1]:
            print(f"Journey from {journey.origin} to {journey.destination} \
will close the crossing at {crossing_times[0]} and re-open at {crossing_times[1]}")

# Testing
get_crossing_events(1432)

