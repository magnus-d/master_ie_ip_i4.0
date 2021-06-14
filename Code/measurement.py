from dht import DHT11
import LED
from machine import Pin, UART
import time


class MHZ19BSensor:
    # Die Basis dieser Class sind verschiedene GitHub Repositories, aus denen wir alle für uns relevanten Informationen
    # gezogen haben.

    # initializes a new instance
    def __init__(self, rx_pin=16, tx_pin=17):
        self.uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1, tx=int(tx_pin), rx=int(rx_pin))

    # measure CO2
    def measure(self):
        while True:
            # send a read command to the sensor
            self.uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')

            # a little delay to let the sensor measure CO2 and send the data back
            time.sleep(1)  # in seconds

            # read and validate the data
            buf = self.uart.read(9)
            if self.is_valid(buf):
                break
        co2 = buf[2] * 256 + buf[3]
        return co2

    # check data returned by the sensor
    def is_valid(self, buf):
        if buf is None or buf[0] != 0xFF or buf[1] != 0x86:
            return False
        i = 1
        checksum = 0x00
        while i < 8:
            checksum += buf[i] % 256
            i += 1
        checksum = ~checksum & 0xFF
        checksum += 1
        return checksum == buf[8]

def temp_hum_measurement():
    # Mit dieser Funktion werden Temperatur und Luftfeuchtigkeit gemessen
    sensor = DHT11(Pin(33))
    time.sleep(2)
    sensor.measure()
    time.sleep(1)
    temp_measure = sensor.temperature()
    hum_measure = sensor.humidity()
    # Aufruf der LED-Funktion temp_hum_corridor
    LED.temp_hum_corridor(temp_measure, hum_measure)
    return temp_measure, hum_measure

def carbon_dioxide_measurement():
    # Mit dieser Funktion wird der CO2-Gehalt der Luft gemessen
    sensor = MHZ19BSensor()
    co2_measure = sensor.measure()
    # Aufruf der LED-Funktion ampel
    LED.ampel(co2_measure)
    return co2_measure

def measurement_start():
    print("\nProgram starts")
    sensor = MHZ19BSensor()
    # Start der Stopuhr
    start = time.ticks_ms()
    # Initialisierung des Stoppdeltas
    delta = 0
    button_d = False
    window = False
    # Aufheizen von 1 Minute zum Messstart
    while delta < 60:
        LED.pin_d6.on()
        time.sleep(1)
        LED.pin_d6.off()
        time.sleep(1)
        co2_measure = sensor.measure()
        LED.ampel(co2_measure)
        time.sleep(1)
        temp_measure, hum_measure = temp_hum_measurement()
        time.sleep(1)
        # Erfassen des Stoppdeltas in Sekunden
        delta = time.ticks_diff(time.ticks_ms(), start) / 1000
        print("\nPreheat time: ", round(delta,2), "seconds")
        print("CO2: ", co2_measure, "ppm",
              "\nTemperature: ", temp_measure, "°C",
              "\nHumidity: ", hum_measure, "%")
    return button_d, window

def measurement_stop():
    # Diese Funktion schaltet zum Ende der Messung alle LED´s aus
    print("Program stopped")
    # alle LED´s aus
    LED.LED_reset()
    for i in range(3):
        LED.pin_d6.on()
        time.sleep(1)
        LED.pin_d6.off()
        time.sleep(1)
    # Boolean für Fenster: False
    window = False
    return window