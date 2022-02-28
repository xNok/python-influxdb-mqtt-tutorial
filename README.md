# Python MQTT Tutorial - Store IoT Metrics with InfluxDB

## Setup

```
pip install requirements.txt
```

Create a file `.env`

```
INFLUXDB_USERNAME=admin
INFLUXDB_PASSWORD=admin1234
INFLUXDB_TOKEN=F-QFQpmCL9UkR3qyoXnLkzWj03s6m4eCvYgDl1ePfHBf9ph7yxaSgQ6WN0i9giNgRTfONwVMK1f977r_g71oNQ==
INFLUXDB_URL="http://localhost:8086"
```

Start InfluxDB

```
docker-compose --env-file .env up
```

In a new shell start the smart sensor:

```
python smart_sensor.py
```

In a third shell start the consumer

```
python influxdb_consumer.py
```

```
python smart_sensor.py
```
