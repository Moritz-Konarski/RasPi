#!/usr/bin/python
import sys, re, os
from time import sleep
import RPi.GPIO as GPIO

light_limit = 200000    # maximum values of the light-value-variable

GPIO.setmode(GPIO.BCM)

pin = 14

value = 0
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)
sleep(0.1)
GPIO.setup(pin, GPIO.IN)
while (GPIO.input(pin) == GPIO.LOW and value < light_limit):
    value += 1
print(value)