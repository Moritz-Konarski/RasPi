from time import sleep
import RPi.GPIO as GPIO

interval = 1

class LED:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def blink(self, n_times=None):
        if n_times is not None:
            for n in range(n_times):
                GPIO.output(self.pin, 1)  # on
                sleep(interval)
                GPIO.output(self.pin, 0)
                sleep(interval)
        else:
            GPIO.output(self.pin, 1)  # on
            sleep(interval)
            GPIO.output(self.pin, 0)
            sleep(interval)
