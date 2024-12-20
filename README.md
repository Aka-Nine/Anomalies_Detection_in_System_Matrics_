

# **Anomaly Detection in Hardware Metrics**

## **Overview**

This project demonstrates how to generate synthetic hardware monitoring data, inject anomalies into it, and detect these anomalies using machine learning. The focus is on simulating system metrics like **CPU temperature**, **CPU usage**, **memory usage**, **battery level**, and **CPU power** to replicate real-world hardware monitoring scenarios.

The project utilizes the **Isolation Forest** algorithm, an unsupervised anomaly detection method, to identify unusual system behavior. Anomalies are then visualized in the generated dataset, enabling insights into system performance and behavior under different conditions.

---

## **Why This Project is Useful**
- **Synthetic Data Generation**: Provides a method to simulate real-world hardware metrics without needing access to live monitoring data.
- **Anomaly Detection**: Demonstrates how to use machine learning to identify outliers or unexpected system behaviors.
- **Data Visualization**: Offers a clear way to interpret anomalies in complex datasets using plots.
- **Scalable Implementation**: Handles large datasets efficiently by processing data in chunks and optimizing memory usage.

---

## **How It Works**

### **Step 1: Synthetic Data Generation**
The dataset is generated by simulating hardware metrics for a defined duration. Here's how it is done:
1. **Timestamps**: Simulated timestamps represent real-time system monitoring.
2. **Metrics**: The following metrics are generated using random values within realistic ranges:
   - **CPU Temperature**: Values between 30°C and 80°C.
   - **CPU Usage**: Values between 0% and 100%.
   - **CPU Load**: Values between 0% and 10%.
   - **Memory Usage**: Values between 20% and 90%.
   - **Battery Level**: Values between 10% and 100%.
   - **CPU Power**: Values between 5W and 50W.
3. **Anomaly Injection**: Random anomalies are injected with a 10% probability. Examples include:
   - CPU usage spikes to 90%-100%.
   - CPU temperature spikes to 90°C-105°C.
   - Memory usage increases to 95%-100%.
   - Battery levels drop to 0%-10%.
   - Power usage spikes to 50W-100W.

The generated data is saved as a **CSV file** (`hardware_monitor_data.csv`).

---

### **Step 2: Anomaly Detection**
The **Isolation Forest** algorithm is applied to detect anomalies in the generated dataset. Here's the process:
1. **Model Training**: The Isolation Forest model is trained on each feature of the dataset.
2. **Anomaly Flagging**: The model assigns an "anomaly" label to data points that significantly deviate from the norm.
3. **Chunk Processing**: For large datasets, the model processes data in chunks to avoid memory constraints.

---

### **Step 3: Data Visualization**
The detected anomalies are visualized in plots for each system metric:
- **Regular Data**: Shown in **blue lines**.
- **Anomalies**: Highlighted as **red dots**.

The dataset is downsampled for clearer visualization, and anomalies are plotted on top of the data to provide insights into unusual system behaviors.

---

## **How to Use This Project**

### **Prerequisites**
1. Python 3.8 or above.
2. Libraries: Install the required libraries using:
   ```bash
   pip install pandas matplotlib scikit-learn psutil wmi
   ```

### **Steps to Run**
1. **Generate the Dataset**:
   - Use the [dataset generation code](#) (Provided in the repo) to create the synthetic dataset.
   - Customize the duration (`duration_minutes`) and sampling rate (`sampling_rate_hz`) to fit your requirements.
   - Run the script to generate the `hardware_monitor_data.csv` file.

2. **Detect Anomalies**:
   - Use the [anomaly detection code](#) (Provided in the repo) to process the generated dataset.
   - The script will detect anomalies and output a list of flagged data points.

3. **Visualize Anomalies**:
   - The script generates plots for each system metric, highlighting anomalies in red and regular data in blue.

---

## **Code Explanation**

### **1. Dataset Generation**
The dataset is generated using random values for each metric. Anomalies are injected with controlled randomness to simulate real-world behavior. The output file is a large CSV that can scale to 1GB or more.

### **2. Anomaly Detection**
Anomalies are detected using the Isolation Forest algorithm. The model flags points that deviate significantly from the norm.

### **3. Plotting**
Plots are generated for each feature:
- Blue lines represent regular data.
- Red dots highlight anomalies detected by the model.

---

## **Example Plot**
![SMAD](https://github.com/user-attachments/assets/8e350c03-8245-48b9-bfcd-43a89606c31f)
*This image shows anomalies (red dots) detected in system metrics (e.g., CPU temperature, memory usage).*

---

## **Conclusion**
This project demonstrates how synthetic data can be used for anomaly detection experiments. It combines data generation, anomaly detection, and visualization to provide a complete workflow for monitoring system performance.

Feel free to customize the code for your own experiments and applications!

