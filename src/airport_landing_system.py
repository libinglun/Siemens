from datetime import datetime, timedelta

class Airport:
    def __init__(self, name: str):
        self.id = name
        self.in_use: bool = False
        self._landing_time: datetime = None

    @property
    def landing_time(self):
        return self._landing_time

    @landing_time.setter
    def landing_time(self, new_landing_time):
        self._landing_time = new_landing_time


class AirportLandingSystem:
    def __init__(self, airports: list[Airport], waiting_interval=60):
        self.airports: dict[str: Airport] = {airport.id: airport for airport in airports}
        # TODO: waiting_interval might be Airport's attribute
        self.waiting_interval: int = waiting_interval

    def request_landing(self, airport_id: str) -> tuple[bool, int]:
        """Check if it is possible to land at the input airport"""
        if airport_id not in self.airports.keys():
            return False, 0

        current_time = datetime.now()
        last_landing_time = self.airports[airport_id].landing_time

        if last_landing_time is None:
            self.airports[airport_id].landing_time = current_time
            return True, 0

        elapsed = int((current_time - last_landing_time).total_seconds())
        if elapsed >= self.waiting_interval:
            self.airports[airport_id].landing_time = current_time
            return True, 0
        else:
            return False, self.waiting_interval - elapsed




