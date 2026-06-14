import sqlite3

DB_NAME = "data/energy_monitor.db"

def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS energy_logs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        room TEXT,
        appliance TEXT,
        status TEXT,
        voltage REAL,
        current REAL,
        power REAL,
        energy REAL,
        cost REAL,
        carbon REAL,
        alert TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appliances(

        appliance TEXT PRIMARY KEY,
        room TEXT,
        power_rating REAL,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_energy(data):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO energy_logs(
    timestamp,room,appliance,status,
    voltage,current,power,
    energy,cost,carbon,alert
    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        data["timestamp"],
        data["room"],
        data["appliance"],
        data["status"],
        data["voltage"],
        data["current"],
        data["power"],
        data["energy"],
        data["cost"],
        data["carbon"],
        data["alert"]
    ))

    conn.commit()
    conn.close()