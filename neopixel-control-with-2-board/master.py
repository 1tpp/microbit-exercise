from microbit import *

import radio
radio.on()
radio.config(channel=42)
radio.config(power=7)

toggleMode = False
indexOfLED = 16
bightness = 255
color = 0
mode = ""

while True:
    potv01 = pin1.read_analog()
    potv02 = pin2.read_analog()

    if button_a.was_pressed():
        toggleMode = not toggleMode
        if toggleMode:
            mode = "C"
        elif toggleMode == False:
            mode = "L"

    if mode == "C":
        indexOfLED = int(potv01 / 64)

    if mode == "L":
        bightness = int(potv02 / 4)

    if button_b.was_pressed():
        if color < 6:
            color +=1
        else:
            color = 0
        radio.send("{0},{1},{2},{3}".format("B", color, indexOfLED, bightness))
        display.show("B")
        sleep(400)

    display.show(mode)
    print(mode, color, indexOfLED, bightness)

    radio.send("{0},{1},{2},{3}".format(mode, color, indexOfLED, bightness))
    sleep(80)
    display.clear()