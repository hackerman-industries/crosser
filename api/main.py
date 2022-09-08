from model.crossing import Crossing
from model.journey import Journey
from journey_utils import get_all_journeys, SERVICES, DATE

def get_crossing_events(time):
    """
    """
    crossing = Crossing("HAZ", 4, 2, 3)

    journeys = get_all_journeys(SERVICES, DATE)

    for journey in journeys:
        crossing_times = crossing.get_journey_crossing_times(journey)
        
        if crossing_times["closure_time"] <= time <= crossing_times["opening_time"]:
            print(f"Journey from {journey.origin} to {journey.destination} \
will close the crossing at {crossing_times['closure_time']} and re-open at {crossing_times['opening_time']}")

# Testing
get_crossing_events(1432)

