import sqlite3

conn = sqlite3.connect("data/energy_monitor.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appliances (
    appliance TEXT PRIMARY KEY,
    room TEXT,
    power REAL,
    status TEXT
)
""")

cursor.executemany(
    """
    INSERT OR REPLACE INTO appliances
    VALUES (?, ?, ?, ?)
    """,
    [
        ("AC", "Bedroom", 1500, "ON"),
        ("Fan", "Bedroom", 80, "ON"),
        ("TV", "Living Room", 120, "OFF"),
        ("Refrigerator", "Kitchen", 250, "ON"),
        ("Washing Machine", "Utility", 500, "OFF"),
        ("Water Heater", "Bathroom", 2000, "OFF")
    ]
)

conn.commit()
conn.close()

print("Appliances table created successfully.")