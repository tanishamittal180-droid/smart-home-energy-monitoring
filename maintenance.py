import sqlite3
import pandas as pd

DB_NAME = "data/energy_monitor.db"

def health_report():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql(
        "SELECT * FROM energy_logs",
        conn
    )

    conn.close()

    results = []

    for appliance in df["appliance"].unique():

        temp = df[
            df["appliance"] == appliance
        ]

        avg_power = temp["power"].mean()

        if avg_power > 1500:

            health = "Critical"

        elif avg_power > 800:

            health = "Warning"

        else:

            health = "Healthy"

        results.append(
            {
                "Appliance": appliance,
                "Health": health
            }
        )

    return pd.DataFrame(results)