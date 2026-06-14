import sqlite3

DB_NAME = "data/energy_monitor.db"

def run_automation():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    appliances = cursor.execute(
        "SELECT * FROM appliances"
    ).fetchall()

    total_power = 0

    for appliance in appliances:

        power_rating = appliance[2]

        status = appliance[3]

        if status == "ON":

            total_power += power_rating

    recommendations = []

    if total_power > 4000:

        recommendations.append(
            "High Power Usage Detected"
        )

    if total_power > 5000:

        recommendations.append(
            "Turn OFF Water Heater"
        )

    if total_power > 6000:

        recommendations.append(
            "Turn OFF AC"
        )

    conn.close()

    return recommendations