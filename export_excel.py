import sqlite3
import pandas as pd

DB_NAME = "data/energy_monitor.db"

def export_excel():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql(
        "SELECT * FROM energy_logs",
        conn
    )

    conn.close()

    df.to_excel(
        "reports/energy_report.xlsx",
        index=False
    )

    return True