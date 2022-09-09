"""Model for a train journey"""
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
        self.journey_length = self.arrival_time - self.departure_time

    def calculate_journey_length(self) -> int:
        """
        Calculates journey length for a journey.
        """
        return self.arrival_time - self.departure_time

    def update_journey_time(self, departure_time, arrival_time):
        """
        Updates the departure and arrival time for a journey.

        Args:
            departure_time: New departure time for the journey.
            arrival_time: New arrival time for the journey.
        """
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.journey_length = self.calculate_journey_length()
