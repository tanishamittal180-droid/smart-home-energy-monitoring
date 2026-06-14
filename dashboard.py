# ==========================
# IMPORTS
# ==========================

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
from analytics import (
    daily_usage,
    room_usage,
    appliance_usage,
    monthly_bill_prediction,
    detect_anomalies
)
from report_generator import generate_pdf
from export_excel import export_excel
from maintenance import health_report
from notifications import get_notifications
import random
try:
    from automation import run_automation
except:
    def run_automation():
        return []
st.sidebar.title(
    "⚡ Energy Intelligence Center"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Analytics",
        "AI Insights"
    ]
)
st.sidebar.header("⚙ Admin Panel")
st.markdown("---")

st.header("🔔 Notification Center")

notifications = get_notifications()

for note in notifications:

    st.info(note)
# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="Smart Home Energy Monitor",
    page_icon="⚡",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

DB_NAME = "data/energy_monitor.db"

# ==========================
# DATABASE FUNCTIONS
# ==========================
def create_appliance_table():
    
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS appliances (
        appliance TEXT PRIMARY KEY,
        room TEXT,
        power REAL,
        status TEXT
    )
    """)

    conn.commit()

    conn.close()

create_appliance_table()
def load_data():

    try:
        conn = sqlite3.connect(DB_NAME)

        df = pd.read_sql(
            "SELECT * FROM energy_logs ORDER BY id DESC",
            conn
        )

        conn.close()

        return df

    except:

        return pd.DataFrame()


def get_appliances():
    
    try:

        conn = sqlite3.connect(DB_NAME)

        rows = conn.execute(
            "SELECT * FROM appliances"
        ).fetchall()

        conn.close()

        return rows

    except Exception as e:

        st.warning(
            f"Appliances table not found: {e}"
        )

        return []

def update_status(appliance, status):

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        UPDATE appliances
        SET status=?
        WHERE appliance=?
        """,
        (status, appliance)
    )

    conn.commit()

    conn.close()

# ==========================
# LOAD DATA
# ==========================

df = load_data()

if df.empty:

    st.warning("Run main.py first to generate data.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"])

latest = df.iloc[0]

# ==========================
# HEADER
# ==========================

st.title("⚡ Smart Home Energy Monitoring System")

st.markdown("---")

# ==========================
# KPI SECTION
# ==========================

total_power = round(df["power"].sum(), 2)
total_energy = round(df["energy"].sum(), 2)
total_cost = round(df["cost"].sum(), 2)
total_carbon = round(df["carbon"].sum(), 2)

c1, c2, c3, c4 = st.columns(4)

c1.metric("⚡ Total Power", f"{total_power:.2f} W")
c2.metric("🔋 Energy Used", f"{total_energy:.2f} kWh")
c3.metric("💰 Cost", f"₹ {total_cost:.2f}")
c4.metric("🌍 Carbon", f"{total_carbon:.2f} kg")

st.markdown("---")

st.header("📅 Daily Energy Analytics")

daily_df = daily_usage()

if not daily_df.empty:

    fig = px.line(
        daily_df,
        x="timestamp",
        y="energy",
        title="Daily Energy Consumption"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
st.markdown("---")

st.header("📊 Executive Summary")
c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Devices",
    len(
        df["appliance"].unique()
    )
)

c2.metric(
    "Rooms",
    len(
        df["room"].unique()
    )
)

c3.metric(
    "Alerts",
    len(
        df[df["alert"]!="NORMAL"]
    )
)

c4.metric(
    "Records",
    len(df)
)
# ==========================
# SMART HOME CONTROL CENTER
# ==========================

st.markdown("---")

st.header("🎮 Smart Home Control Center")

appliances = get_appliances()

if appliances:

    for appliance in appliances:

        name = appliance[0]
        room = appliance[1]
        power = appliance[2]
        status = appliance[3]

        a, b, c, d = st.columns([3,2,2,2])

        a.write(f"⚡ {name}")
        b.write(room)
        c.write(f"{power} W")

        if status == "ON":

            if d.button(
                f"Turn OFF {name}",
                key=f"off_{name}"
            ):
                update_status(name, "OFF")
                st.rerun()

        else:

            if d.button(
                f"Turn ON {name}",
                key=f"on_{name}"
            ):
                update_status(name, "ON")
                st.rerun()

else:

    st.info("No appliances found.")

# ==========================
# DIGITAL TWIN
# ==========================

st.markdown("---")

st.header("🏠 Advanced Digital Twin")
room_power = (
    df.groupby("room")["power"]
    .sum()
)

cols = st.columns(
    len(room_power)
)

for i, room in enumerate(room_power.index):

    power = room_power[room]

    if power < 500:

        emoji = "🟢"

    elif power < 2000:

        emoji = "🟡"

    else:

        emoji = "🔴"

    cols[i].metric(
        f"{emoji} {room}",
        f"{power:.0f}W"
    )

# ==========================
# AUTOMATION ENGINE
# ==========================

st.markdown("---")

st.header("🧠 Smart Recommendations")

recommendations = run_automation()

if recommendations:

    for rec in recommendations:

        st.warning(rec)

else:

    st.success("Energy Usage Optimized")

# ==========================
# CURRENT STATUS
# ==========================

st.markdown("---")

st.subheader("📡 Latest Reading")

s1, s2, s3, s4, s5 = st.columns(5)

s1.metric("Room", latest["room"])
s2.metric("Appliance", latest["appliance"])
s3.metric("Voltage", f"{latest['voltage']} V")
s4.metric("Current", f"{latest['current']} A")
s5.metric("Power", f"{latest['power']} W")

# ==========================
# POWER TREND
# ==========================

st.markdown("---")

st.subheader("📈 Power Trend")

fig = px.line(
    df.head(100),
    x="timestamp",
    y="power"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================
# ROOM ANALYSIS
# ==========================

st.subheader("🏠 Room Analysis")

room_df = (
    df.groupby("room")["power"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    room_df,
    x="room",
    y="power"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================
# APPLIANCE ANALYSIS
# ==========================

st.subheader("🔌 Appliance Ranking")

app_df = (
    df.groupby("appliance")["power"]
    .sum()
    .reset_index()
)

app_df = app_df.sort_values(
    by="power",
    ascending=False
)

fig3 = px.bar(
    app_df,
    x="appliance",
    y="power"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================
# PIE CHART
# ==========================

st.subheader("🥧 Appliance Contribution")

fig4 = px.pie(
    app_df,
    names="appliance",
    values="power"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ==========================
# LIVE GAUGE
# ==========================

st.subheader("⚡ Live Power Gauge")

fig5 = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=float(latest["power"]),
        gauge={
            "axis": {
                "range":[0,2500]
            }
        }
    )
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# ==========================
# ALERTS
# ==========================

st.subheader("🚨 Alerts")

alerts = df[df["alert"] != "NORMAL"]

if not alerts.empty:

    st.dataframe(alerts.head(20))

else:

    st.success("No Active Alerts")

# ==========================
# RAW DATA
# ==========================

with st.expander("📂 View Database"):

    st.dataframe(df)
st.markdown("---")

st.header("🤖 AI Bill Prediction")

predicted_bill = monthly_bill_prediction()

c1,c2 = st.columns(2)

c1.metric(
    "Current Cost",
    f"₹ {total_cost:.2f}"
)

c2.metric(
    "Predicted Monthly Bill",
    f"₹ {predicted_bill:.2f}"
)
st.markdown("---")

st.header("🌍 Carbon Analytics")
carbon_today = round(
    df["carbon"].sum(),
    2
)

trees_needed = round(
    carbon_today / 21,
    2
)

c1,c2 = st.columns(2)

c1.metric(
    "CO₂ Produced",
    f"{carbon_today} kg"
)

c2.metric(
    "Trees Needed",
    trees_needed
)
st.markdown("---")

st.header("⏰ Peak Usage Analysis")
peak_record = df.loc[
    df["power"].idxmax()
]

st.metric(
    "Highest Power Consumption",
    f"{peak_record['power']} W"
)

st.write(
    "Peak Time:",
    peak_record["timestamp"]
)

st.write(
    "Appliance:",
    peak_record["appliance"]
)
st.markdown("---")

st.header("🚨 AI Anomaly Detection")
anomalies = detect_anomalies()

if not anomalies.empty:

    st.error(
        f"{len(anomalies)} abnormal energy events detected"
    )

    st.dataframe(
        anomalies.tail(20)
    )

else:

    st.success(
        "No anomalies detected"
    )
st.markdown("---")

st.header("🏆 Energy Intelligence")
top_device = (
    df.groupby("appliance")["power"]
    .sum()
    .idxmax()
)

worst_room = (
    df.groupby("room")["power"]
    .sum()
    .idxmax()
)

st.info(
    f"Highest consuming appliance: {top_device}"
)

st.warning(
    f"Highest consuming room: {worst_room}"
)
st.markdown("---")

st.header("⚡ Energy Efficiency")
avg_power = df["power"].mean()

efficiency = max(
    0,
    100 - avg_power/50
)

st.progress(
    int(min(efficiency,100))
)

st.metric(
    "Efficiency Score",
    f"{efficiency:.1f}/100"
)
if st.sidebar.button(
    "Generate PDF Report"
):

    generate_pdf()

    st.sidebar.success(
        "PDF Report Created"
    )
if st.sidebar.button(
    "Export Excel"
):

    export_excel()

    st.sidebar.success(
        "Excel Export Completed"
    )
st.markdown("---")

st.header("🏥 Appliance Health Monitor")
health_df = health_report()

st.dataframe(
    health_df,
    use_container_width=True
)
st.markdown("---")

st.header("👨‍👩‍👧 Occupancy Analytics")
rooms = [
    "Living Room",
    "Bedroom",
    "Kitchen",
    "Bathroom",
    "Study Room"
]

occupancy = []

for room in rooms:

    occupancy.append(
        {
            "Room": room,
            "People":
            random.randint(0,5)
        }
    )

occ_df = pd.DataFrame(
    occupancy
)

fig_occ = px.bar(
    occ_df,
    x="Room",
    y="People",
    title="Room Occupancy"
)

st.plotly_chart(
    fig_occ,
    use_container_width=True
)
# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.success("System Running Successfully")
