import time

from .airport_landing_system import Airport, AirportLandingSystem

def count_down(remaining_time: int):
    while remaining_time > 0:
        print(f"Next landing in: {remaining_time:3d} seconds", end='\r')
        time.sleep(1)
        remaining_time -= 1
    print("-----Landing is now allowed.")

def simulate_landing_system(system: AirportLandingSystem):
    while True:
        airport_id = input("Enter the airport ID where the aircraft will land (LGW, EMA, MAN): ")
        if airport_id not in system.airports.keys():
            print("Invalid airport ID.")
            continue

        can_land, remain_time = system.request_landing(airport_id)
        if can_land:
            print(f"-----Landing at {airport_id} is confirmed.")
        else:
            print(f"-----Landing is not possible. Please Wait for {remain_time} seconds.")
            count_down(remain_time)
            can_land, _ = system.request_landing(airport_id)
            if can_land:
                print(f"-----Landing at {airport_id} is confirmed after waiting.")
            else:
                raise ValueError('Landing failed after waiting')

if __name__ == '__main__':
    airports_id = ["LGW", "EMA", "MAN"]
    system = AirportLandingSystem([Airport(name) for name in airports_id], waiting_interval=20)

    simulate_landing_system(system)

