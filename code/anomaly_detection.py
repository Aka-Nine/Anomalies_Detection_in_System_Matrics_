import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Path to the large CSV file
file_path = 'D:/ML/hardware_monitor_data.csv'

# Define the required features for analysis
required_features = ['cpu_temperature', 'cpu_usage', 'cpu_load', 'memory_usage', 'battery_level', 'cpu_power']

# Initialize an empty DataFrame to store anomalies
anomalies_df = pd.DataFrame()

# Read and process the dataset in chunks
chunk_size = 100000  
chunk_iter = pd.read_csv(file_path, chunksize=chunk_size)

for chunk in chunk_iter:
    # Ensure required features are present
    for feature in required_features:
        if feature not in chunk.columns:
            raise ValueError(f"Feature '{feature}' is missing from the dataset!")

    # Prepare the data for anomaly detection 
    chunk = chunk[required_features].fillna(0)

    # Train the Isolation Forest model on the chunk
    model = IsolationForest(contamination=0.1, random_state=42)
    chunk['anomaly'] = model.fit_predict(chunk)
    chunk['is_anomaly'] = chunk['anomaly'] == -1

    # Append anomalies to the anomalies DataFrame
    anomalies_df = pd.concat([anomalies_df, chunk[chunk['is_anomaly']]])

# Report total anomalies detected
total_anomalies = anomalies_df.shape[0]
print(f"Total anomalies detected: {total_anomalies}")

# Downsample the main dataset for plotting
df = pd.read_csv(file_path, usecols=required_features, nrows=500000)  # Limit to first 500k rows for plotting
df = df.iloc[::100]  # Downsample every 100th row
df = df.fillna(0)  # Fill missing values with 0

# Adjust the index of anomalies to match the downsampled dataset
anomalies_df = anomalies_df.loc[anomalies_df.index.intersection(df.index)]

# Plot each feature with anomalies highlighted
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 12))
axes = axes.flatten()

for i, feature in enumerate(required_features):
    ax = axes[i]

    # Plot smoothed data
    ax.plot(df.index, df[feature], label='Smoothed Data', color='blue', linewidth=0.7)

    # Highlight anomalies
    feature_anomalies = anomalies_df[anomalies_df[feature].notna()]
    ax.scatter(feature_anomalies.index, feature_anomalies[feature], color='red', label='Anomalies', s=10)

    # Set titles and labels
    ax.set_title(f"{feature.capitalize()} with Anomalies Highlighted")
    ax.set_xlabel('Index')
    ax.set_ylabel(feature.capitalize().replace('_', ' '))
    ax.legend()

# Remove extra subplots
for j in range(len(required_features), len(axes)):
    fig.delaxes(axes[j])

# Adjust layout and display the plot
fig.suptitle("Anomalies Detection in System Metrics", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
