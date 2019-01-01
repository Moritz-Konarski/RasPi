#!/usr/bin/python
import sys, Adafruit_DHT, re, os
from time import sleep
import RPi.GPIO as GPIO

light_limit = 200000

GPIO.setmode(GPIO.BCM)

def dht_measure(pin):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    humidity = round(humidity * 100) / 100
    temperature = round(temperature * 100) / 100
    return temperature, humidity

def dht_name(n=int):
    temp_name = "Temp_{}".format(n)
    hum_name = "Hum_{}".format(n)
    return temp_name, hum_name

def outdoor_temp_measure(address):

    path = "/sys/bus/w1/devices/" + address + "/w1_slave"

    with open(path, "r") as file:
        read = file.readlines()

    while "NO\n" in read[0]:
        sleep(.25)
        with open(path, "r") as file:
            read = file.readlines()

    for read_line in read:
        if "t=" in read_line:
            nums = [float(s) for s in re.findall(r'-?\d+\.?\d*', read_line)]
            temp = round(nums[-1] / 100) / 10

    return temp

def light_measure(pin):
        value = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        sleep(0.1)
        GPIO.setup(pin, GPIO.IN)
        while (GPIO.input(pin) == GPIO.LOW and value < light_limit):
            value += 1
        return value

class Dht22:

    def __init__(self, pins=[]):
        self.pins = pins
        self.names = [dht_name(n) for n, m in enumerate(pins)]
    
    def measure(self):
        self.values = [dht_measure(pin) for pin in self.pins]

class OutdoorTemp:

    def __init__(self, addresses=[]):
        self.addresses = addresses
        self.names = ["OutdoorTemp_{}".format(n) for n, m in enumerate(addresses)]
        os.system("modprobe w1-gpio")
        os.system("modprobe w1-therm")

    def measure(self):
        self.values = [outdoor_temp_measure(address) for address in self.addresses]

class Light: 

    def __init__(self, pins=[]):
        self.pins = pins
        self.names = ["Light_{}".format(n) for n, m in enumerate(pins)]

    def measure(self):
        self.values = [light_measure(pin) for pin in self.pins]