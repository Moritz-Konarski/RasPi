"""
Relevant funtions:

dht = Dht_22(pins)
dht.measure()

light = Light(pins)
light.measure()

relevant values:

dht.temp_hum_values
dht.temp_hum_names

light.names
light.values
"""
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT

def light_measure(pin):
        value = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        sleep(0.1)
        GPIO.setup(pin, GPIO.IN)
        while (GPIO.input(pin) == GPIO.LOW and value < 100000):
            value += 1
        return value

def dht_measure(pin):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    temp = round(temperature * 10) / 10
    hum = round(humidity * 10) / 10
    return temp, hum

def dht_name(n):
    temp = "Temp {}".format(n + 1)
    hum = "Hum {}".format(n + 1)
    return temp, hum

class Dht_22:

    def __init__(self, pins=[]):
        self.pins = pins
        self.temp_hum_names = [dht_name(n) for n in range(len(pins))]
    
    def measure(self):
        self.temp_hum_values = [dht_measure(pin) for pin in self.pins]

class Light: 

    def __init__(self, pins=[]):
        self.pins = pins
        self.names = ["Light {}".format(n + 1) for n in range(len(pins))]
    
    def measure(self):
        self.values = [light_measure(pin) for pin in self.pins]