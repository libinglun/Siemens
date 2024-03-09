import random
import unittest
from datetime import datetime, timedelta

from src import AirportLandingSystem, Airport


class TestAirportLandingSystem(unittest.TestCase):

    def setUp(self):
        airports_id = ["LGW", "EMA", "MAN"]
        self.system = AirportLandingSystem([Airport(name) for name in airports_id], waiting_interval=60)
        self.current_time = datetime.now()

    def test_initial_state(self):
        """All airports should be available initially for landing"""
        for airport in self.system.airports:
            self.assertTrue(self.system.request_landing(airport))

    def test_landing_at_busy_airport(self):
        """Landing should be unsuccessful if busy"""
        elapse = timedelta(seconds=random.randint(1, 59))
        self.system.airports["EMA"].set_landing_time(self.current_time - elapse)
        can_land, _ = self.system.request_landing("EMA")
        self.assertFalse(can_land)

    def test_landing_after_waiting(self):
        """ After waiting for 60 seconds, landing should be successful"""
        self.system.airports["MAN"].set_landing_time(self.current_time - timedelta(seconds=60))
        can_land, _ = self.system.request_landing('MAN')
        self.assertTrue(can_land)

        self.system.airports["MAN"].set_landing_time(self.current_time - timedelta(seconds=59))
        can_land, _ = self.system.request_landing('MAN')
        self.assertFalse(can_land)

    def test_invalid_airport_id(self):
        can_land, _ = self.system.request_landing("XYZ")
        self.assertFalse(can_land)
