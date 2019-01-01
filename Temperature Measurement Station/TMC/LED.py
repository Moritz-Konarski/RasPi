#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

interval = 1

class LEDIndicator:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def blink(self, n_times=1):
        for n in range(n_times):
            GPIO.output(self.pin, 1)  # on
            sleep(interval)
            GPIO.output(self.pin, 0)  # off
            sleep(interval)

    @property
    def on(self):
        GPIO.output(self.pin, 1)  # on

    @property
    def off(self):
        GPIO.output(self.pin, 0)  # off