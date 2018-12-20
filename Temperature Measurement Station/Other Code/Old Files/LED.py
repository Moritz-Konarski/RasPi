import sys, os, Adafruit_DHT
from time import sleep
import datetime as dt
from subprocess import call
import RPi.GPIO as GPIO
import lcddriver
from time import * 
#lcd = lcddriver.lcd()
#lcd.lcd_clear()
GPIO.setmode(GPIO.BCM)

pin = 18
pin2 = 14
print("output set")
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, 1)

for n in range(0, 5):
	GPIO.output(pin, 1)
	sleep(1)
	GPIO.output(pin, 0)
	sleep(1)
	n = n+1

for n in range(0, 3):
	print("HIGH - off")
	GPIO.output(pin2, 1)
	sleep(2)
	print("LOW - on")
	GPIO.output(pin2, 0)
	sleep(2)
	print("--------")
	n = n+1

GPIO.output(pin2, 0)
print("lightlevel")
reading = 0
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
sleep(0.1)
GPIO.setup(23, GPIO.IN)
while (GPIO.input(23) == GPIO.LOW and reading < 100000):
	reading += 1
print("temperature")
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 24)
print("done")
print(str(reading) + "\n" + str(temperature) + " | " + str(humidity))

GPIO.output(pin2, 1)

GPIO.cleanup()