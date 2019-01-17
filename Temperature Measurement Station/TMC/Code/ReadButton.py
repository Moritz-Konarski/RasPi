
# this program detects when a button is pushed and then switches on the lcd backlight

import RPi.GPIO as GPIO
from time import sleep

pinNum = 17
ledNum = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum, GPIO.IN) 
GPIO.setup(ledNum, GPIO.OUT)

def switch_backlight(channel):
    GPIO.output(ledNum, GPIO.HIGH)
    sleep(10)
    GPIO.output(ledNum, GPIO.LOW)

GPIO.add_event_detect(pinNum, GPIO.RISING, callback=switch_backlight, bouncetime=200) 

while True:
    sleep(1)
