from machine import Pin
import LED
import measurement

def Keypad_Button():
    # Mit dieser Funktion wird der auf dem Keypad gedrückte Button ermittelt und für die weitere Verarbeitung zurückgegeben
    button = "None"
    row_1 = Pin(21, Pin.OUT)
    row_2 = Pin(19, Pin.OUT)
    row_3 = Pin(18, Pin.OUT)
    row_4 = Pin(5, Pin.OUT)
    column_1 = Pin(0, Pin.IN, Pin.PULL_UP)
    column_2 = Pin(2, Pin.IN, Pin.PULL_UP)
    column_3 = Pin(15, Pin.IN, Pin.PULL_UP)
    column_4 = Pin(8, Pin.IN, Pin.PULL_UP)
    value_column_1 = column_1.value()
    value_column_2 = column_2.value()
    value_column_3 = column_3.value()
    value_column_4 = column_4.value()
    row_1 = Pin(21, Pin.IN, Pin.PULL_UP)
    row_2 = Pin(19, Pin.IN, Pin.PULL_UP)
    row_3 = Pin(18, Pin.IN, Pin.PULL_UP)
    row_4 = Pin(5, Pin.IN, Pin.PULL_UP)
    column_1 = Pin(0, Pin.OUT)
    column_2 = Pin(2, Pin.OUT)
    column_3 = Pin(15, Pin.OUT)
    column_4 = Pin(8, Pin.OUT)
    value_row_1 = row_1.value()
    value_row_2 = row_2.value()
    value_row_3 = row_3.value()
    value_row_4 = row_4.value()

    if value_row_4 == False and value_column_4 == False:
        button = "D"
    elif value_row_4 == False and value_column_3 == False:
        button = "#"
    elif value_row_4 == False and value_column_2 == False:
        button = "0"
    elif value_row_4 == False and value_column_1 == False:
        button = "*"
    elif value_row_3 == False and value_column_4 == False:
        button = "C"
    elif value_row_3 == False and value_column_3 == False:
        button = "9"
    elif value_row_3 == False and value_column_2 == False:
        button = "8"
    elif value_row_3 == False and value_column_1 == False:
        button = "7"
    elif value_row_2 == False and value_column_4 == False:
        button = "B"
    elif value_row_2 == False and value_column_3 == False:
        button = "6"
    elif value_row_2 == False and value_column_2 == False:
        button = "5"
    elif value_row_2 == False and value_column_1 == False:
        button = "4"
    elif value_row_1 == False and value_column_4 == False:
        button = "A"
    elif value_row_1 == False and value_column_3 == False:
        button = "3"
    elif value_row_1 == False and value_column_2 == False:
        button = "2"
    elif value_row_1 == False and value_column_1 == False:
        button = "1"
    return button

def user_input(button_d, window):
    button_d = button_d
    window = window
    # Aufruf des Tastenfeldes
    button = Keypad_Button()
    # Abwesenheit (Knopf D)
    if button == "D":
        measurement.measurement_stop()
        button_d = True
    # Fensterschließung quittieren (Knopf C)
    elif button == "C":
        # 7-Color-Flash aus & Boolean für Fenster: False
        window = LED.window_closed()
    # Fensteröffnung quittieren (Knopf B)
    elif button == "B":
        # 7-Color-Flash an & Boolean für Fenster: True
        window = LED.window_open()
    return button_d, window