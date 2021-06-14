# Begrüßung des Users
print("\n\nHello User")
# Import der benötigten Bibliotheken und Unterprogramme
print("Importing libraries and programs...")
import time
time.sleep(1)
import wifi
time.sleep(1)
import Keypad
time.sleep(1)
import measurement
print("...Import ready")

# Zunächst muss einmal das WLAN und der MQTT-Client connected werden.
# Außerdem muss die RTC synchronisiert und die Intervalle festgelegt werden
time.sleep(1)
wifi.wifi_connect()  # WLAN-Connection herstellen
time.sleep(1)
wifi.synchronize_rtc()  # Real-Time-Clock synchronisieren
time.sleep(1)
mqtt_client = wifi.connect_mqtt()
time.sleep(1)
interval_1 = 300  # Messintervall 1 beträgt 5 min (300 sek)
interval_2 = 150  # Messintervall 2 beträgt 2,5 min (150 sek)

# Solange der Mikrocontroller nicht vom Strom getrennt wird, läuft diese Schleife
while True:
    print("Waiting for the start of the measurement")
    # Gedrückten Knopf ermitteln
    button = Keypad.Keypad_Button()

    # Anwesenheit quittiert (Knopf A wurde gedrückt)
    if button == "A":
        # Messprogramm startet, Sensor wird aufgeheizt
        button_d, window = measurement.measurement_start()

        # Unterbrechung des Programms, wenn Knopf D gedrückt wird
        while not button_d == True:
            # Aufruf der Messfunktion carbon_dioxide_measurement
            co2_measure = measurement.carbon_dioxide_measurement()
            time.sleep(1)
            # Aufruf der Messfunktion temp_hum_measurement
            temp_measure, hum_measure = measurement.temp_hum_measurement()
            time.sleep(1)
            # Aufruf der Sendefunktion aws_connection
            wifi.aws_connection(mqtt_client, temp_measure, hum_measure, co2_measure)
            time.sleep(1)
            # Start der Stopuhr
            start = time.ticks_ms()
            # Initialisierung des Stoppdeltas
            delta = 0
            # Wenn das Fenster geschlossen ist...
            if window == False:
                # Messintervall 1 bei geschlossenem Fenster
                while delta < interval_1:
                    # Funktion für die verschiedenen Input-Möglichkeiten des Users
                    button_d, window = Keypad.user_input(button_d, window)
                    time.sleep(0.5)
                    # Erfassen des Stoppdeltas in Sekunden
                    delta = time.ticks_diff(time.ticks_ms(), start) / 1000
            # Wenn das Fenster geöffnet ist...
            elif window == True:
                # Messintervall 2 geöffnetem Fenster
                while delta < interval_2:
                    # Funktion für die verschiedenen Input-Möglichkeiten des Users
                    button_d, window = Keypad.user_input(button_d, window)
                    time.sleep(0.5)
                    # Erfassen des Stoppdeltas in Sekunden
                    delta = time.ticks_diff(time.ticks_ms(), start) / 1000
    time.sleep(0.5)