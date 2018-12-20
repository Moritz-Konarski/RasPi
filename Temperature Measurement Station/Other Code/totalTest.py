import sys, os, Adafruit_DHT
from time import sleep
import datetime as dt
import RPi.GPIO as GPIO
from time import *
import lcddriver

GPIO.setmode(GPIO.BCM)

pinLed = 18
pinRelay = 14
pinLight = 23
pinTemp = 24

GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinRelay, GPIO.OUT)
GPIO.output(pinRelay, 0)
sleep(1)

lcd = lcddriver.lcd()
lcd.lcd_clear()

def LcdPrint(string1, string2):
    lcd.lcd_clear()
    lcd.lcd_display_string(str(string1), 1)
    lcd.lcd_display_string(str(string2), 2)

print("output set")
sleep(2)
print("led")
for n in range(0, 5):
	GPIO.output(pinLed, 1)
	sleep(.5)
	GPIO.output(pinLed, 0)
	sleep(.5)
	n = n+1

print("relay")
for n in range(0, 2):
    print("LOW - on")
    GPIO.output(pinRelay, 0)
    sleep(2)
    print("HIGH - off")
    GPIO.output(pinRelay, 1)
    sleep(2)
    n = n+1

GPIO.output(pinRelay, 0)
print("light level")
reading = 0
GPIO.setup(pinLight, GPIO.OUT)
GPIO.output(pinLight, GPIO.LOW)
sleep(0.1)
GPIO.setup(pinLight, GPIO.IN)
while (GPIO.input(pinLight) == GPIO.LOW and reading < 100000):
	reading += 1
sleep(2)
print("temperature")
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pinTemp)
print("done")
temperature = round(temperature, 2)
humidity = round(humidity, 2)
print(str(reading) + "\n" + str(temperature) + " | " + str(humidity))
LcdPrint(str(temperature) + " | " + str(humidity), str(reading))
sleep(10)

LcdPrint("Shutting", "Down")
sleep(3)
lcd.lcd_backlight("OFF")
lcd.lcd_clear()
sleep(.5)
GPIO.output(pinRelay, 1)
GPIO.cleanup()