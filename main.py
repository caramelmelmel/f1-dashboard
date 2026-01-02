import fastf1
import pandas as pd

# Enable caching (recommended)
#fastf1.Cache.enable_cache('cache')

# Load session data
session = fastf1.get_session(2024, 'Bahrain', 'Q')  # year, grand prix name, session (FP1, FP2, FP3, Q, R)
session.load()

# Get lap times
laps = session.laps

# Get telemetry for a specific driver
driver_laps = session.laps.pick_driver('VER')

print("Session loaded successfully!")
print(f"Total laps: {len(laps)}")
print(f"\nFastest lap:")
print(laps.pick_fastest()) 
print(driver_laps)