import network
from umqtt.robust import MQTTClient
import json
import time
import ntptime

CERT_FILE = "cert\cert.der"
KEY_FILE = "cert\private.der"

# Hier müssen Ihre Pfade und Daten ergänzt werden
MQTT_CLIENT_ID = "Hier den Namen des IoT-Devices bei AWS eintragen"
MQTT_PORT = 8883
MQTT_TOPIC = "Hier das MQTT-Topic eintragen"
MQTT_HOST = "Hier die Adresse des MQTT-Hosts eintragen"

def wifi_connect():
    # Mit dieser Funktion wird die WIFI-Verbindung hergestellt
    print("Connecting to WIFI")

    # Hier müssen Ihre WIFI-Informationen ergänzt werden
    WIFI_SSID = "Hier den Namen des WLAN-Netzwerks eintragen"
    WIFI_PW = "Hier das Passwort des WLAN-Netzwerks eintragen"

    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(WIFI_SSID, WIFI_PW)
        while not wlan.isconnected():
            pass

    print("connected:", WIFI_SSID)

def synchronize_rtc():
    ntptime.settime()
    print("Time synchronised")

def current_datetime():
    ts = time.localtime()
    return '{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}'.format(ts[0], ts[1], ts[2], ts[3], ts[4], ts[5])

def aws_connection(mqtt_client,temp_measure, hum_measure, co2_measure):
    try:
        pub_msg(mqtt_client, air_quality_data_msg(temp_measure, hum_measure, co2_measure))

        print("timestamp: ", current_datetime(),
              "\ntemperature: ", temp_measure, "°C",
              "\nhumidity: ", hum_measure, "%",
              "\ncarbon_dioxide: ", co2_measure, "ppm")

    except Exception as e:
        print(str(e))

def pub_msg(mqtt_client, msg):
    try:
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("\nSent data to AWS:")
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

def air_quality_data_msg(temp_measure, hum_measure, co2_measure):
    datetime = current_datetime()
    try:
        message = {'temperature': temp_measure,
                       'humidity': hum_measure,
                   'carbon_dioxide': co2_measure,
                   'timestamp': datetime}
    except Exception as e:
        message = {'error': "Error reading air quality data: " + str(e)}
    return json.dumps(message)

def connect_mqtt():
    try:
        with open(KEY_FILE, "r") as f:
            key = f.read()
        print("Got Key")

        with open(CERT_FILE, "r") as f:
            cert = f.read()
        print("Got Cert")

        mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000,
                                 ssl=True,
                                 ssl_params={"cert": cert, "key": key, "server_side": False})
        mqtt_client.connect()
        print('MQTT Connected')

        return mqtt_client

    except Exception as e:
        print('Cannot connect MQTT: ' + str(e))
        raise
