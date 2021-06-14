from machine import Pin
from time import sleep

# 7_Color_Flash
pin_d1 = Pin(32, Pin.OUT)
pin_d1.off()

# SMD_RGB_LED
pin_d2 = Pin(25, Pin.OUT)  # red
pin_d3 = Pin(26, Pin.OUT)  # green
pin_d2.off()
pin_d3.off()

# RGB_LED
pin_d4 = Pin(14, Pin.OUT)  # blue
pin_d5 = Pin(12, Pin.OUT)  # red
pin_d6 = Pin(13, Pin.OUT)  # green
pin_d4.off()
pin_d5.off()
pin_d6.off()

# Two_Color_LED
pin_d7 = Pin(27, Pin.OUT)  # yellow
pin_d7.off()

def RGB_reset():
    # Diese Funktion schaltet die RBG LED ab
    pin_d4.off()
    pin_d5.off()
    pin_d6.off()

def LED_reset():
    # Diese Funktion schaltet alle LED`s ab
    pin_d1.off()
    pin_d2.off()
    pin_d3.off()
    RGB_reset()
    pin_d7.off()

def window_open():
    # Mithilfe dieser Funktion wird signalisiert, dass das Fenster geöffnet ist
    print("Window open")
    pin_d1.on()
    window = True
    return window

def window_closed():
    # Mithilfe dieser Funktion wird signalisiert, dass das Fenster geöffnet ist
    print("Window closed")
    pin_d1.off()
    window = False
    return window

def ampel(co2_measure):
    # Wenn Messwert CO2 unter 800: grün
    if co2_measure < 800:
        pin_d2.off()
        pin_d3.on()
        pin_d7.off()

    # Wenn Messwert CO2 zwischen 800 und 1000: gelb
    elif co2_measure < 1400:
        pin_d2.off()
        pin_d3.off()
        pin_d7.on()

    # Wenn Messwert CO2 über 1000: rot
    elif co2_measure > 1400:
        pin_d2.on()
        pin_d3.off()
        pin_d7.off()

def temp_hum_corridor(temp_measure, hum_measure):
    temp_min = 19
    temp_max = 25
    hum_min = 40
    hum_max = 60
    RGB_reset()
    if temp_measure < temp_min:
        for i in range(5):
            pin_d4.on()
            sleep(1)
            pin_d4.off()
            sleep(1)
        print("Temperature low")
        pin_d4.on()
    elif hum_measure < hum_min:
        for i in range(5):
            pin_d4.on()
            sleep(1)
            pin_d4.off()
            sleep(1)
        print("Humidity low")
        pin_d4.on()
    elif temp_measure > temp_max:
        for i in range(5):
            pin_d5.on()
            sleep(1)
            pin_d5.off()
            sleep(1)
        print("Temperature high")
        pin_d5.on()
    elif hum_measure > hum_max:
        for i in range(5):
            pin_d5.on()
            sleep(1)
            pin_d5.off()
            sleep(1)
        print("Humidity high")
        pin_d5.on()
    else:
        print("Temperature & humidity are fine")
        pin_d6.on()