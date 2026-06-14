# ⚡ Smart Home Energy Monitoring System

## 📌 Project Overview

The Smart Home Energy Monitoring System is an IoT-based energy management platform that monitors, analyzes, and predicts household electricity consumption. The system simulates smart appliances, calculates power usage, energy consumption, electricity costs, and carbon emissions, and visualizes the data through an interactive Streamlit dashboard.

The project also includes advanced features such as AI-based bill prediction, anomaly detection, appliance health monitoring, occupancy analytics, smart recommendations, digital twin visualization, PDF report generation, and Excel export.

This project demonstrates concepts of IoT, Smart Homes, Energy Analytics, Automation, Data Visualization, Machine Learning, and Dashboard Development.

---

# 🎯 Objectives

- Monitor energy consumption in real time.
- Calculate power, energy, electricity cost, and carbon emissions.
- Detect abnormal energy usage.
- Predict future electricity bills.
- Generate reports and analytics.
- Provide smart recommendations for energy savings.
- Simulate a smart home environment without physical hardware.
- Build a professional IoT dashboard suitable for portfolios and internships.

---

# 🚀 Features

## Energy Monitoring

- Real-time power monitoring
- Energy consumption tracking
- Electricity cost estimation
- Carbon emission calculation
- Historical energy analysis

## Smart Home Dashboard

- Interactive Streamlit Dashboard
- Appliance monitoring
- Room-wise energy analysis
- Live power gauge
- Smart Home Digital Twin

## AI Analytics

- Monthly bill prediction
- Energy forecasting
- Peak usage detection
- Appliance intelligence
- Energy efficiency scoring
- Anomaly detection

## Smart Home Automation

- Appliance status monitoring
- Occupancy simulation
- Energy optimization recommendations
- Alert generation system

## Reporting

- PDF Report Generation
- Excel Export
- Energy Consumption Logs
- Historical Reports

## Maintenance

- Appliance Health Monitoring
- Predictive Maintenance
- Notification Center

---

# 🏗 System Architecture

```text
Virtual Appliances
        │
        ▼
Energy Simulator
        │
        ▼
Power & Energy Calculation
        │
        ▼
SQLite Database
        │
        ▼
Analytics Engine
        │
        ▼
AI Prediction Engine
        │
        ▼
Automation Engine
        │
        ▼
Streamlit Dashboard
        │
        ▼
Reports & Alerts
```

---

# 🛠 Technologies Used

## Programming Language

- Python

## Database

- SQLite

## Dashboard

- Streamlit
- Plotly

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-Learn

## Reports

- ReportLab
- OpenPyXL

---

# 📂 Project Structure

```text
Smart-Home-Energy-Monitoring-System/

│
├── dashboard.py
├── main.py
│
├── analytics.py
├── automation.py
├── maintenance.py
├── notifications.py
├── report_generator.py
├── export_excel.py
├── voice_assistant.py
│
├── data/
│   ├── energy_monitor.db
│   └── energy_log.csv
│
├── reports/
│   ├── energy_report.pdf
│   └── energy_report.xlsx
│
├── outputs/
│
├── images/
│
├── README.md
└── requirements.txt
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Smart-Home-Energy-Monitoring-System.git
```

```bash
cd Smart-Home-Energy-Monitoring-System
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit pandas numpy plotly scikit-learn reportlab openpyxl streamlit-autorefresh
```

---

# ▶ Running the Project

## Step 1

Run Energy Simulation

```bash
python main.py
```

---

## Step 2

Launch Dashboard

```bash
streamlit run dashboard.py
```

---

# 📊 Dashboard Modules

## Executive Summary

Displays:

- Total Power Consumption
- Total Energy Usage
- Electricity Cost
- Carbon Emission

---

## Smart Home Control Center

Displays:

- Appliance Status
- Room Information
- Device Controls

---

## Digital Twin

Displays:

- Room-wise Power Usage
- Smart Building Visualization

---

## Analytics Dashboard

Displays:

- Daily Energy Usage
- Room Analytics
- Appliance Analytics
- Carbon Analytics
- Peak Usage Analytics

---

## AI Insights

Displays:

- Monthly Bill Prediction
- Anomaly Detection
- Energy Efficiency Score
- Appliance Intelligence

---

## Reports

Generate:

- PDF Reports
- Excel Reports

---

# 📈 Energy Calculations

## Power Calculation

```text
Power (W) = Voltage × Current
```

Example:

```text
Voltage = 230V
Current = 2A

Power = 460W
```

---

## Energy Calculation

```text
Energy (kWh) = Power (kW) × Time (Hours)
```

Example:

```text
1000W appliance running for 5 hours

Energy = 5 kWh
```

---

## Cost Calculation

```text
Cost = Energy × Tariff
```

Example:

```text
10 kWh × ₹8

Cost = ₹80
```

---

# 🤖 AI Features

## Monthly Bill Prediction

Uses Linear Regression to estimate future electricity bills.

## Anomaly Detection

Detects unusual power consumption patterns.

## Appliance Intelligence

Identifies:

- Highest consuming appliance
- Highest consuming room

## Energy Efficiency Score

Provides a score out of 100 based on energy usage.

---

# 🌍 Carbon Analytics

The system estimates carbon emissions generated due to electricity consumption.

Formula:

```text
Carbon Emission = Energy × Emission Factor
```

Used for:

- Sustainability Analysis
- Environmental Monitoring
- Energy Optimization

---

# 🏥 Predictive Maintenance

The system analyzes appliance energy usage patterns and classifies devices as:

- Healthy
- Warning
- Critical

This helps identify appliances that may require maintenance.

---

# 📄 Report Generation

Supported Formats:

## PDF

Contains:

- Energy Logs
- Appliance Information
- Consumption Records

## Excel

Contains:

- Complete Database Export
- Energy Consumption History

---

# 📸 Screenshots Checklist

Capture screenshots of:

- Streamlit Dashboard
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130640" src="https://github.com/user-attachments/assets/def7660d-179c-4b9a-9eb0-069c0b19b3a5" />

- KPI Cards
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130657" src="https://github.com/user-attachments/assets/e7a50ae0-4372-49e4-bfab-262f57890668" />

- Power Trend Graph
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130707" src="https://github.com/user-attachments/assets/2f0fa2b7-0b9c-4399-95a1-2a02fd28ee4c" />

- Energy Trend Graph
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130720" src="https://github.com/user-attachments/assets/44a2f073-d5cf-4644-94da-d87d78ce56ce" />

- Room Analysis
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130728" src="https://github.com/user-attachments/assets/843cd63f-1fd8-438b-8e1a-f0c2d9d565a0" />

- Appliance Analysis
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130737" src="https://github.com/user-attachments/assets/30439bf5-16f8-4c25-882b-2a69620fa245" />

- Live Gauge
- Alert Center
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130750" src="https://github.com/user-attachments/assets/bef51185-d148-4230-b0e7-31bc687abe34" />

- Digital Twin
- AI Insights
- <img width="1366" height="768" alt="Screenshot 2026-06-13 130758" src="https://github.com/user-attachments/assets/b52eed05-860e-44e7-8420-ab077956680d" />

- PDF Report
- Excel Report
<img width="1366" height="768" alt="Screenshot 2026-06-13 131117" src="https://github.com/user-attachments/assets/52c32c0e-b82a-41bf-ad5c-4e1c019ef8e3" />


---

# 🔮 Future Enhancements

- MQTT Integration
- Real IoT Sensor Integration
- ESP32 Support
- ThingSpeak Dashboard
- Blynk Integration
- Mobile Application
- Voice Assistant Control
- Smart Meter Integration
- Solar Energy Monitoring
- Deep Learning Forecasting
- Home Assistant Integration

---

# 🎓 Learning Outcomes

Through this project, I learned:

- IoT System Design
- Smart Home Automation
- Energy Monitoring
- Database Management
- Dashboard Development
- Data Analytics
- Machine Learning
- Predictive Maintenance
- Report Generation
- Python Development

---

# 💼 Resume Keywords

- IoT
- Smart Home
- Energy Monitoring
- Streamlit
- Python
- SQLite
- Data Analytics
- Machine Learning
- Dashboard Development
- Predictive Analytics
- Automation
- Digital Twin
- Energy Forecasting
- Smart Building
- Sustainability Analytics

---

# 🎤 Interview Questions

### Explain your project.

The Smart Home Energy Monitoring System is an IoT-inspired platform that monitors and analyzes household electricity consumption. It calculates power, energy, cost, and carbon emissions, stores data in SQLite, and visualizes information using Streamlit dashboards. The system also includes AI-based bill prediction, anomaly detection, appliance health monitoring, occupancy analytics, digital twin visualization, and automated report generation.

### Why did you choose SQLite?

SQLite is lightweight, easy to integrate with Python, and suitable for local IoT simulations.

### How is power calculated?

Power is calculated using:

```text
Power = Voltage × Current
```

### How is energy consumption calculated?

Energy is calculated using:

```text
Energy = Power × Time
```

### What machine learning algorithm did you use?

Linear Regression for monthly bill prediction.

### How does anomaly detection work?

Power values above a calculated threshold are marked as anomalies.

### What are the benefits of this system?

- Reduces electricity waste
- Lowers electricity bills
- Improves energy efficiency
- Supports predictive maintenance

---

# 👩‍💻 Author

Tanisha Mittal

Smart Home Energy Monitoring System

IoT | Python | Streamlit | Data Analytics | Machine Learning

---

# ⭐ If you like this project

Please star the repository and share feedback.
