"""Model for a train crossing"""
class Crossing():
    """
    Class to represent a train crossing.
    """
    def __init__(self, crossing_location, arrival_offset, departure_offset, closure_length):
        self.crossing_location = crossing_location
        self.arrival_offset = arrival_offset
        self.departure_offset = departure_offset
        self.closure_length = closure_length

    def get_journey_crossing_times(self, journey):
        closure_time = journey.departure_time + self.departure_offset if self.crossing_location == journey.origin \
            else journey.arrival_time - self.arrival_offset

        return {
            "closure_time": closure_time,
            "opening_time": (closure_time + self.closure_length)
        }

