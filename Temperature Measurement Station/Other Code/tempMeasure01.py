#!/usr/bin/python

#importing libraries
import sys, os, Adafruit_DHT
from time import sleep
import datetime as dt
from subprocess import call
import RPi.GPIO as GPIO
from shutil import copyfile

GPIO.setmode(GPIO.BCM)                  #setting GPIO mode to chip-designations

#defining variables
led_pin=23                              #pin of the LED
temp_pin=[22,27,17]                     #pins of the temp sensors
light_pin=[18,15,14]                    #pins of the light sensors

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
    while (GPIO.input(pin) == GPIO.LOW and reading < 100000):
        reading += 1
    light[n]=reading

def READING():                          #defining a fuction to read all three pairs of sensors
    for n in range(3):
        LIGHT(light_pin[n], n)
        LED(4)
        TEMP(temp_pin[n], n)
        LED(4)

#the programm
try:
    start_time = dt.datetime.now()
    file_name = start_time.strftime("%c") + "-log" 
    file=open("/home/pi/Desktop/" + file_name + ".txt", "a")
    #file.write("Date Time,Temp 1,Temp 2,Temp 3,Hum 1,Hum 2,Hum 3,Light 1,Light 2,Light 3\n")
    
    for rev in range(0,50):
        print(str(rev))
        for r in range(0,3):                    
            READING()
            for q in range(3):
                sum_temp[r][q]=temp[q]
                sum_hum[r][q]=hum[q]
                sum_light[r][q]=light[q]
            LED(4)
            LED(4)
            LED(4)

        for i in range(3):
            for j in range(3):
                avrg_temp[i]+=sum_temp[j][i]
                avrg_hum[i]+=sum_hum[j][i]
                avrg_light[i]+=sum_light[j][i]

        for t in range(3):
            avrg_temp[t]=round(avrg_temp[t]/3, 1)
            avrg_hum[t]=round(avrg_hum[t]/300, 3)
            avrg_light[t]=avrg_light[t]/3

        now_time = dt.datetime.now()
        date_time = now_time.strftime("%x") + " " + now_time.strftime("%X")
        
        file.write(date_time + ",")
        for wn in range(0,3):
            file.write(str(avrg_temp[wn]) + ",")
        for wn in range(0,3):
            file.write(str(avrg_hum[wn]) + ",")
        for wn in range(0,2):
            file.write(str(avrg_light[wn]) + ",")
        file.write(str(avrg_light[2]) + "\n")
        
        #if rev>1 and rev%5==0:
        #    file.close()
        #    copyfile("/home/pi/Desktop/" + file_name + ".txt", "/home/pi/Desktop/" + file_name + "-backup-" + str(rev/5) + ".txt")
        #    file=open("/home/pi/Desktop/" + file_name + ".txt", "a")

        avrg_temp=[0,0,0]                       
        avrg_hum=[0,0,0]                        
        avrg_light=[0,0,0]                      

        for wait in range(0,5):
            LED(10)

    file.close()
    sleep(1)
except KeyboardInterrupt:
    print("\nUser terminated Programm.")
    file.close()
finally:
    print("Done!")
    GPIO.cleanup()
    #call("cd /Desktop/Data")
    #call("sudo cat *.txt >> summary.txt")
    call("sudo reboot", shell=True)