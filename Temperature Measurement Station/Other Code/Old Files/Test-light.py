#importing libraries
import sys, os, Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

#setting GPIO mode to chip-designations
GPIO.setmode(GPIO.BCM)

light_pin_3=16


reading = 0
GPIO.setup(light_pin_3, GPIO.OUT)
GPIO.output(light_pin_3, GPIO.LOW)
sleep(0.1)
GPIO.setup(light_pin_3, GPIO.IN)
while (GPIO.input(light_pin_3) == GPIO.LOW):
        reading += 1
print(str(reading))
GPIO.cleanup()
