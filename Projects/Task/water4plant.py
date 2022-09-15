import time
import board
import digitalio
import analogio

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

sensorPower = digitalio.DigitalInOut(board.GP16)
sensorPower.direction = digitalio.Direction.OUTPUT
sensorPower.value = False

pump = digitalio.DigitalInOut(board.GP10)
pump.direction = digitalio.Direction.OUTPUT
pump.value = False
pump2 = digitalio.DigitalInOut(board.GP11)
pump2.direction = digitalio.Direction.OUTPUT
pump2.value = False
pump3 = digitalio.DigitalInOut(board.GP12)
pump3.direction = digitalio.Direction.OUTPUT
pump3.value = False

sensor = analogio.AnalogIn(board.A0)

# <288 dry --- >33000 water
while True:
  sensorPower.value = True
  sensorvalue = sensor.value
  sensorPower.value = False
  if sensorvalue < 588:
    pump.value = True
    pump2.value = True
    pump3.value = True
    led.value = True
  if sensorvalue > 33000:
    led.value = False
    pump.value = False
    pump2.value = False
    pump3.value = False
  time.sleep(600)
