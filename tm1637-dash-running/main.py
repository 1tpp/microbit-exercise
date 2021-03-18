from microbit import *
import tm1637

tm = tm1637.TM1637(clk=pin15, dio=pin16)

patterns = [
    [0x01, 0x00, 0x00, 0x00],
    [0x00, 0x01, 0x00, 0x00],
    [0x00, 0x00, 0x01, 0x00],
    [0x00, 0x00, 0x00, 0x01],
    [0x00, 0x00, 0x00, 0x02],
    [0x00, 0x00, 0x00, 0x04],
    [0x00, 0x00, 0x00, 0x08],
    [0x00, 0x00, 0x08, 0x00],
    [0x00, 0x08, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
]

step = 0
toggleMode = True
mode = "Clockwise"
pause = False

while True:
    if button_a.was_pressed():
        toggleMode = not toggleMode
        if toggleMode:
            mode = "Clockwise"
        elif toggleMode == False:
            mode = "CounterClockwise"

    if mode == "Clockwise":
        if step < len(patterns) - 1:
            step += 1
        else:
            step = 0
    if mode == "CounterClockwise":
        if step > 0:
            step -= 1
        else:
            step = len(patterns) - 1

    if button_b.was_pressed():
        pause = True
        while pause:
            tm.write(patterns[step])
            if button_b.was_pressed():
                pause = False

    print(step)
    tm.write(patterns[step])
    sleep(100)
