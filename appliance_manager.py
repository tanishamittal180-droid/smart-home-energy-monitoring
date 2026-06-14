import sqlite3

DB_NAME = "data/energy_monitor.db"

APPLIANCES = [

    ("TV","Living Room",120),
    ("Fan","Living Room",80),
    ("Lights","Living Room",60),

    ("AC","Bedroom",1500),
    ("Laptop","Bedroom",90),

    ("Microwave","Kitchen",1200),
    ("Refrigerator","Kitchen",250),
    ("Water Heater","Kitchen",2000),

    ("Computer","Study Room",250),
    ("Printer","Study Room",100)
]

def initialize_appliances():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    for appliance in APPLIANCES:

        cursor.execute("""
        INSERT OR IGNORE INTO appliances
        VALUES(?,?,?,?)
        """,
        (
            appliance[0],
            appliance[1],
            appliance[2],
            "ON"
        ))

    conn.commit()
    conn.close()


def get_appliances():

    conn = sqlite3.connect(DB_NAME)

    rows = conn.execute(
        "SELECT * FROM appliances"
    ).fetchall()

    conn.close()

    return rows


def update_status(name,status):

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        UPDATE appliances
        SET status=?
        WHERE appliance=?
        """,
        (status,name)
    )

    conn.commit()
    conn.close()