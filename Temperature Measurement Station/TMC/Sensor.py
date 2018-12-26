import sys, Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

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
    humidity = round(humidity * 100) / 100
    temperature = round(temperature * 100) / 100
    return temperature, humidity

def dht_name(n):
    temp_name = "Temp {}".format(n + 1)
    hum_name = "Hum {}".format(n + 1)
    return temp_name, hum_name

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

