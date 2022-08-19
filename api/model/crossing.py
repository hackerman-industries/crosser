class Crossing():
    """
    Class to represent a train crossing.

    arrival_offset, departure_offset -> these describe the number of minutes after departure or before
    arrival that crossing closes. These could be the same value.

    closure_length -> the length of time the crossing is actually down for, unsure if this is always
    the same
    """
    def __init__(self, crossing_location, arrival_offset, departure_offset, closure_length):
        self.crossing_location = crossing_location
        self.arrival_offset = arrival_offset
        self.departure_offset = departure_offset
        self.closure_length = closure_length
    
    def calculate_journey_crossing_time(self, journey):
        if self.crossing_location == journey.origin:
            closure_time = journey.departure_time + self.departure_offset
            return [closure_time, (closure_time + self.closure_length)]
        elif self.crossing_location == journey.destination:
            closure_time = journey.arrival_time - self.arrival_offset
            return [closure_time, (closure_time + self.closure_length)]
