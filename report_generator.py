import sqlite3
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

DB_NAME = "data/energy_monitor.db"


def generate_pdf():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql(
        "SELECT * FROM energy_logs",
        conn
    )

    conn.close()

    doc = SimpleDocTemplate(
        "reports/energy_report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Smart Home Energy Monitoring Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    table_data = [list(df.columns)]

    for row in df.tail(100).values:
        table_data.append(list(row))

    table = Table(table_data)

    table.setStyle(
        TableStyle([
            ('GRID',(0,0),(-1,-1),1,colors.black),
            ('BACKGROUND',(0,0),(-1,0),colors.lightgrey)
        ])
    )

    elements.append(table)

    doc.build(elements)

    return True