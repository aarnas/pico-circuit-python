import board
import adafruit_dht

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

dht = adafruit_dht.DHT11(board.GP28)

temperature = dht.temperature
humidity = dht.humidity

layout.write("temperature: " + str(temperature))
layout.write(" humidity: " + str(humidity))