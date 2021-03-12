from microbit import *
import neopixel
np = neopixel.NeoPixel(pin14, 16)

import radio
radio.on()
radio.config(channel=42)
radio.config(power=7)

mode = ""
color = 0
indexOfLED = 0
bightness = 0

def setColor(color, bightness):
    colors = [
        (bightness, 0, 0),
        (bightness, bightness, 0),
        (0, bightness, 0),
        (bightness, 0, bightness),
        (0, 0, bightness),
        (0, bightness, bightness),
        (bightness, bightness, bightness),
    ]
    return colors[color]

while True:
    data = radio.receive()
    if data != None:
        dataList = data.split(",")
        mode = str(dataList[0])
        color = int(dataList[1])
        indexOfLED = int(dataList[2])
        bightness = int(dataList[3])

        print(mode, color, indexOfLED, bightness)

    for led in range(indexOfLED):
        np[led] = setColor(color, bightness)
    np.show()

    if indexOfLED > 1:
        np[indexOfLED - 1] = (0,0,0)

    display.show(mode)