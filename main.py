from src import *

airports_id = ["LGW", "EMA", "MAN"]
system = AirportLandingSystem([Airport(name) for name in airports_id], waiting_interval=20)

simulate_landing_system(system)