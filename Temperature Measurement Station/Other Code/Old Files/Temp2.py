#!/usr/bin/python

import sys
import Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

pin1 = 22
pin2 = 27
pin3 = 17
interval = 3
n = 0

sensor=Adafruit_DHT.DHT22

def LED (interval, m):
        n=0
        for n in range(0, m):
            GPIO.output(23, 1)
            sleep(interval/2)
            GPIO.output(23, 0)
            sleep(interval/2)
            n=n+1

for n in range(0, 10):

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin1)

    if humidity is not None and temperature is not None:
        print('1: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
    LED(2, 2)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin2)

    if humidity is not None and temperature is not None:
        print(' 2: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
    LED(2, 2)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin3)

    if humidity is not None and temperature is not None:
        print(' 3: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
    LED(2, 2)

    n += 1

GPIO.cleanup()