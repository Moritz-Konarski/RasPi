#!/usr/bin/python

#importing libraries
import sys, os, Adafruit_DHT
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)                  #setting GPIO mode to chip-designations

#defining variables
led_pin=23                              #pin of the LED
temp_pin=[22,27,17]                     #pins of the temp sensors
light_pin=[18,15,14]                    #pins of the light sensors
interv=2                                #interval of the LED blinking

#defining the lists of measurements
temp=[0,0,0]                            #temp measurements
hum=[0,0,0]                             #humidity measurements
light=[0,0,0]                           #light measuremenss
sum_temp=[[0,0,0],[0,0,0],[0,0,0]]      #sum of three measurement passes for temp
sum_hum=[[0,0,0],[0,0,0],[0,0,0]]       #sum of three measurement passes for humindity
sum_light=[[0,0,0],[0,0,0],[0,0,0]]     #sum of three measurement passes for light
avrg_temp=[0,0,0]                       #average of three temp passes
avrg_hum=[0,0,0]                        #average of three humidity passes
avrg_light=[0,0,0]                      #average of three light passes

GPIO.setup(led_pin, GPIO.OUT)           #setting the LED pin to output

def LED (interval):                     #defining LED function
    sleep(interval/2)
    GPIO.output(23, 1)
    sleep(.5)
    GPIO.output(23, 0)
    sleep(interval/2)

def TEMP (pin, n):                      #defining temp/humidity measurement function
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    if humidity is None and temperature is None:
        temp[n]='--No Data--'
        hum[n]='--No Data--'
    else:
        temp[n]=round(temperature*10)/10
        hum[n]=round(humidity*10)/10
        
def LIGHT (pin, n):                     #defining light measurement function
    reading = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW):
            reading += 1
    light[n]=reading

def READING():                          #defining a fuction to read all three pairs of sensors
    for n in range(3):
        LIGHT(light_pin[n], n)
        LED(2)
        TEMP(temp_pin[n], n)
        LED(2)

#the programm
file=open("measure.txt", "a")
file.write("t1,t2,t3,h1,h2,h3,l1,l2,l3;")
for rev in range(0,5):
    for r in range(0,3):                    
        READING()
        # print("Temperature " + str(temp))
        # print("Humidity    " + str(hum))
        # print("Light       " + str(light))
        LED(2)
        for q in range(3):
            sum_temp[r][q]=temp[q]
            sum_hum[r][q]=hum[q]
            sum_light[r][q]=light[q]
        print("-")

    for i in range(3):
        for j in range(3):
            avrg_temp[i]+=sum_temp[j][i]
            avrg_hum[i]+=sum_hum[j][i]
            avrg_light[i]+=sum_light[j][i]

    print("------------------")

    for t in range(3):
        avrg_temp[t]=round(avrg_temp[t]/3, 1)
        avrg_hum[t]=round(avrg_hum[t]/3, 1)
        avrg_light[t]=avrg_light[t]/3

    print("Avrg Temperature " + str(avrg_temp))
    print("Avrg Humidity    " + str(avrg_hum))
    print("Avrg Light       " + str(avrg_light))

    for wn in range(0,2):
        file.write(str(avrg_temp[wn]) + ",")
    for wn in range(0,2):
        file.write(str(avrg_hum[wn]) + ",")
    for wn in range(0,1):
        file.write(str(avrg_light[wn]) + ",")
    file.write(str(avrg_light[2]) + ";")
    #file.write(str(avrg_temp) + "," + str(avrg_hum) + "," + str(avrg_light) + "\n")
    avrg_temp=[0,0,0]                       #average of three temp passes
    avrg_hum=[0,0,0]                        #average of three humidity passes
    avrg_light=[0,0,0]                      #average of three light passes
    # file.write(str(avrg_hum) + ",")
    # file.write(str(avrg_light) + "\n")

file.close()
GPIO.cleanup()