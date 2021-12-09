import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

b_long = 0.5			# Long Blink duration
b_short = 0.2			# Short Blink duration
w_wait = 0.5			# Wait duration between words
a_wait = 0.25			# Wait duration between alphas

m = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morse = m.split(" ")
alpha = 'abcdefghijklmnopqrstuvwxyz'
w_wait = w_wait - a_wait

def long_blink():
    led.value = True
    time.sleep(b_long)
    led.value = False
    time.sleep(a_wait)
    
def short_blink():
    led.value = True
    time.sleep(b_short)
    led.value = False
    time.sleep(a_wait)

word = "sos"

while True:
    for s in word:
        dig = morse[alpha.find(s)]
        for d in dig:
            if d == '.':
                short_blink()
            if d == '-':
                long_blink()
        time.sleep(w_wait)
    time.sleep(1)
        