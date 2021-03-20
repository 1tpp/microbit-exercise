from microbit import *

state = [False, False, False, False, False]
prevState = [False, False, False, False, False]
toggle = [False, False, False, False, False]


def displayLED(col, bightness):
    for row in range(5):
        display.set_pixel(col, row, bightness)


while True:
    distance = int(pin1.read_analog() * 520 / 1024.0)

    for i in range(5):
        minDistance = (i+1)*10
        maxDistance = (i+2)*10

        if distance > minDistance and distance <= maxDistance:
            state[i] = True

        if toggle[i] or state[i]:
            displayLED(i, 9)

        if state[i] != prevState[i] and prevState[i]:
            toggle[i] = not toggle[i]
            if toggle[i] == False:
                displayLED(i, 0)

        prevState[i] = state[i]
        state[i] = False

    print("Sonar = {0} CM".format(distance))
    sleep(200)
