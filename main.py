import time

from database import (
    create_database
)

from appliance_manager import (
    initialize_appliances
)

from automation import (
    generate_sensor_data
)

from mqtt_publisher import (
    publish_sensor_data
)

create_database()

initialize_appliances()

print("IoT Energy Simulator Started")

while True:

    data = generate_sensor_data()

    publish_sensor_data(data)

    print(data)

    time.sleep(3)