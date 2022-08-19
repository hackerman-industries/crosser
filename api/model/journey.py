class Journey:
    """
    Class to represent a train journey.
    """
    def __init__(self, origin, destination, journey_date, departure_time, arrival_time) -> None:
        self.origin = origin
        self.destination = destination
        self.journey_date = journey_date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.journey_length = self.calculate_journey_length()

    def calculate_journey_length(self):
        return self.arrival_time - self.departure_time

