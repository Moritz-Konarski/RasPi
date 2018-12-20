#!/usr/bin/python

#importing libraries
import sys, os, Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

#setting GPIO mode to chip-designations
GPIO.setmode(GPIO.BCM)

#defining the pins
led_pin=23
light_pin_1=18
light_pin_2=15
light_pin_3=14
temp_pin_1=22
temp_pin_2=27
temp_pin_3=17

#setting the LED pin to output
GPIO.setup(led_pin, GPIO.OUT)

#defining variables
interv=2

#setting the LED pin to output
GPIO.setup(led_pin, GPIO.OUT)

#defining LED function
def LED (interval):
    sleep(interval/2)
    GPIO.output(23, 1)
    sleep(.5)
    GPIO.output(23, 0)
    sleep(interval/2)

#defining temp/humidity function
def TEMP (pin):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    if humidity is None and temperature is None:
        print('--No Data--')
    else:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

def LIGHT (pin):
    reading = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW):
            reading += 1
    print(str(reading))

for n in range(0, 15):
    LED (interv)
    print("L1:")
    LIGHT(light_pin_1)
    LED (interv)
    print("L2:")
    LIGHT(light_pin_2)
    LED (interv)
    print("L3:")
    LIGHT(light_pin_3)
    LED (interv)
    print("T1:")
    TEMP(temp_pin_1)
    LED (interv)
    print("T2:")
    TEMP(temp_pin_2)
    LED (interv)
    print("T3:")
    TEMP(temp_pin_3)
    print("--------------------------")
GPIO.cleanup()