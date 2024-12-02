import wmi
import psutil
import pandas as pd
import datetime
import random

# Settings
duration_minutes = 22222  
sampling_rate_hz = 10
num_samples = duration_minutes * 60 * sampling_rate_hz

# Initialize WMI client
w = wmi.WMI(namespace="root\\OpenHardwareMonitor")

# Initialize lists
timestamps = []
cpu_temperatures = []
cpu_usages = []
cpu_loads = []
memory_usages = []
battery_levels = []
cpu_powers = []

# Collect data
for i in range(num_samples):
    try:
        # Generate synthetic timestamp
        current_time = datetime.datetime.now() + datetime.timedelta(seconds=i / sampling_rate_hz)
        timestamps.append(current_time)

        # Simulate sensor data
        cpu_temp = random.uniform(30, 80)
        cpu_power = random.uniform(5, 50)
        cpu_usage = random.uniform(0, 100)
        cpu_load = random.uniform(0, 10)
        memory_usage = random.uniform(20, 90)
        battery_level = random.uniform(10, 100)

        # Append sensor data
        cpu_temperatures.append(cpu_temp)
        cpu_usages.append(cpu_usage)
        cpu_loads.append(cpu_load)
        memory_usages.append(memory_usage)
        battery_levels.append(battery_level)
        cpu_powers.append(cpu_power)

        # Randomly inject anomalies
        if random.random() < 0.1:
            cpu_usages[-1] = random.uniform(90, 100)  # High CPU usage
        if random.random() < 0.1:
            cpu_temperatures[-1] = random.uniform(90, 105)  # High temperature
        if random.random() < 0.1:
            memory_usages[-1] = random.uniform(95, 100)  # High memory usage
        if random.random() < 0.1:
            battery_levels[-1] = random.uniform(0, 10)  # Low battery level
        if random.random() < 0.1:
            cpu_powers[-1] = random.uniform(50, 100)  # High power usage

    except Exception as e:
        print(f"Error collecting data: {e}")
        cpu_temperatures.append(None)
        cpu_usages.append(None)
        cpu_loads.append(None)
        memory_usages.append(None)
        battery_levels.append(None)
        cpu_powers.append(None)

# Save to CSV
data = {
    'timestamp': timestamps,
    'cpu_temperature': cpu_temperatures,
    'cpu_usage': cpu_usages,
    'cpu_load': cpu_loads,
    'memory_usage': memory_usages,
    'battery_level': battery_levels,
    'cpu_power': cpu_powers
}
df = pd.DataFrame(data)
df.to_csv(r'hardware_monitor_data.csv', index=False)

# Confirm file size
import os
file_size = os.path.getsize('hardware_monitor_data.csv') / (1024**2)
print(f"Generated file size: {file_size:.2f} MB")
