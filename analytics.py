import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

DB_NAME = "data/energy_monitor.db"


def load_data():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql(
        "SELECT * FROM energy_logs",
        conn
    )

    conn.close()

    return df


def daily_usage():

    df = load_data()

    if df.empty:
        return pd.DataFrame()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    daily = (
        df.groupby(
            df["timestamp"].dt.date
        )["energy"]
        .sum()
        .reset_index()
    )

    return daily


def room_usage():

    df = load_data()

    if df.empty:
        return pd.DataFrame()

    room_df = (
        df.groupby("room")["power"]
        .sum()
        .reset_index()
    )

    return room_df


def appliance_usage():

    df = load_data()

    if df.empty:
        return pd.DataFrame()

    app_df = (
        df.groupby("appliance")["power"]
        .sum()
        .reset_index()
    )

    return app_df


def monthly_bill_prediction():

    df = load_data()

    if len(df) < 20:
        return 0

    X = np.arange(len(df)).reshape(-1, 1)

    y = df["cost"].cumsum()

    model = LinearRegression()

    model.fit(X, y)

    future = np.array([[len(df)+500]])

    prediction = model.predict(future)

    return round(float(prediction[0]), 2)


def detect_anomalies():

    df = load_data()

    if df.empty:
        return pd.DataFrame()

    threshold = (
        df["power"].mean() +
        2 * df["power"].std()
    )

    anomalies = df[
        df["power"] > threshold
    ]

    return anomalies