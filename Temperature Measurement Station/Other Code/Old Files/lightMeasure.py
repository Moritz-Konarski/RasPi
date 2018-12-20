#test for the light sensor

import RPi.GPIO as GPIO, time, os      
from time import sleep

GPIO.setmode(GPIO.BOARD)

plug1 = 8
plug2 = 10
plug3 = 12
interval = 3
n = 0

def LightLevel (pin):
        
        reading = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(pin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(pin) == GPIO.LOW):
                reading += 1
        #reading = float(reading + 1) 
        return reading

for n in range(0,20):
        print ("Sensor1:     " + str(LightLevel(plug1)))
        sleep(interval)
        print ("  Sensor2:   " + str(LightLevel(plug2)))
        sleep(interval)
        print ("    Sensor3: " + str(LightLevel(plug3)))
        sleep(interval)
        n += 1

GPIO.cleanup()