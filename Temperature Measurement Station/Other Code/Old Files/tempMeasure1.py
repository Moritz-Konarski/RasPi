#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os      
import datetime
from time import sleep
import Adafruit_DHT

DEBUG = 1
GPIO.setmode(GPIO.BCM)
n=0
pin=17
sensor=Adafruit_DHT.DHT22

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

while n<50:                                     
        #print  ("LL: " + str(RCtime(4)))
	lightlevel=RCtime(4)
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	#print ("RH: " + str(humidity) + "%")
	#print ("T: " + str(temperature) + "C")
        print (datetime.datetime.now().isoformat())
	print (str(n) + "  LL: " + str(lightlevel) + "  RH: " + str(round(100*humidity)/100) + " %  T: " + str(round(100*temperature)/100) + " C")
	n=n+1
	sleep(30)
