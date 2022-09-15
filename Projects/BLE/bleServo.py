import time
import board
import busio
import digitalio

import pwmio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

pwm = pwmio.PWMOut(board.GP15, frequency=50)
servo_1 = servo.Servo(pwm)

def parseLine(line):
    if(line[0:5] == "SERVO"):
        servo_1.angle = int(line[6:])
    elif(line[0:5] == "CLICK"):
        servo_1.angle = 20
        time.sleep(0.3)
        servo_1.angle = 160
    
while True:
    data = uart.read(32)
    if data is not None:
        data_string = ''.join([chr(b) for b in data])
        data_string_length = len(data_string)
        if data_string_length > 2:
            parseLine(data_string[0:data_string_length-2])
            data_string_length = 0