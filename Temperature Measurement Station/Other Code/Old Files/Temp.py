import RPi.GPIO as GPIO, time, os      
import datetime
from time import sleep
import Adafruit_DHT


GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
m=0
pin=15
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

def LED (Pin, interval, time):
        GPIO.setup(Pin, GPIO.OUT)
        n=0
        max=int(round(time/interval))
        for n in range(0, max):
                GPIO.output(Pin, 1)
                sleep(interval/2)
                GPIO.output(Pin, 0)
                sleep(interval/2)
                n=n+1
        
while m<100:  
        sleep(.1)                                   
        lightlevel=RCtime(8)
        sleep(.1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        sleep(.1)
        print datetime.datetime.now().isoformat()
        print(str(m))
        print("         LL: " + str(lightlevel))
        print("         RH: " + str(humidity) + " %")
        print("         T: " + str(temperature) + " C")
        m=m+1
        LED(16, .1, 5)
GPIO.cleanup()
