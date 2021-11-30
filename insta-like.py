import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio

mouse = Mouse(usb_hid.devices)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False
counter = 1

progStatus = False
progStatusPin = digitalio.DigitalInOut(board.GP15)
progStatusPin.switch_to_input(pull=digitalio.Pull.UP)
progStatus = not progStatusPin.value

if progStatus == False:
    time.sleep(2)
    mouse.move(0, 0)
    time.sleep(2)
    mouse.move(0, 0)
    time.sleep(1)
    mouse.move(0, 0)

while (counter < 200 and progStatus == False):
    #Scroll
    time.sleep(1)
    mouse.press(Mouse.LEFT_BUTTON)
    mouse.move(y=-44)
    mouse.release(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    #Move mouse back
    mouse.move(y=44)
    time.sleep(0.5)
    #Like
    led.value = True
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.1)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    led.value = False
    counter += 1