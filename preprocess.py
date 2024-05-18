import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 5, 7)

# Define time interval
time_interval = timedelta(minutes=5)

# Generate timestamps
timestamps = pd.date_range(start=start_date, end=end_date, freq=time_interval)

# Node IDs
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialize a list to hold the traffic data
traffic_data = []

# Simulate traffic data
for timestamp in timestamps:
    minute = timestamp.minute
    hour = timestamp.hour
    dow = timestamp.weekday()
    day = timestamp.day
    month = timestamp.month
    
    for node in nodes:
        # Simulate the number of vehicles
        base_traffic = np.random.poisson(20)  # Poisson distribution around a mean value
        peak_traffic = np.random.poisson(40)  # Higher traffic for peak hours
        vehicles = base_traffic
        
        # Increase traffic during rush hours (8-10 AM and 5-7 PM) on weekdays
        if dow < 5:  # Weekday
            if (7 <= hour <= 9) or (16 <= hour <= 18):
                vehicles = peak_traffic
        
        traffic_data.append([timestamp, minute, hour, dow, day, month, node, vehicles])

# Create DataFrame
traffic_df = pd.DataFrame(traffic_data, columns=["timestamp", "minute", "hour", "dow", "day", "month", "node", "vehicles"])

# Save to CSV
traffic_df.to_csv("traffic.csv", index=False)
