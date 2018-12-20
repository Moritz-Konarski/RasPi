#!/usr/bin/python

#importing libraries
import sys, os, Adafruit_DHT
from time import sleep
import datetime as dt
from subprocess import call
import RPi.GPIO as GPIO

#defining pin connections
led_pin=23                              #pin of the LED
temp_pin=[22,27,17]                     #pins of the temp sensors
light_pin=[18,15,14]                    #pins of the light sensors

#setting gpio modes
GPIO.setmode(GPIO.BCM)                  #setting GPIO mode to chip-designations
GPIO.setup(led_pin, GPIO.OUT)           #setting the LED pin to output

#defining variables
temp=[0,0,0]                            #temp measurements
hum=[0,0,0]                             #humidity measurements
light=[0,0,0]                           #light measuremenss
sum_temp=[[0,0,0],[0,0,0],[0,0,0]]      #sum of three measurement passes for temp
sum_hum=[[0,0,0],[0,0,0],[0,0,0]]       #sum of three measurement passes for humindity
sum_light=[[0,0,0],[0,0,0],[0,0,0]]     #sum of three measurement passes for light
avrg_temp=[0,0,0]                       #average of three temp passes
avrg_hum=[0,0,0]                        #average of three humidity passes
avrg_light=[0,0,0]                      #average of three light passes
shutdownVar = False

#defining LED function
def LED (interval):                     
    sleep(interval/2)
    GPIO.output(23, 1)                  #on
    sleep(.5)
    GPIO.output(23, 0)                  #off
    sleep(interval/2)

#defining temp/humidity measurement function
def TEMP (pin, n):                      
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    if humidity is None and temperature is None:
        temp[n]='--No Data--'
        hum[n]='--No Data--'
    else:
        temp[n]=round(temperature*10)/10
        hum[n]=round(humidity*10)/10

#defining light measurement function    
def LIGHT (pin, n):                     
    reading = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW and reading < 100000):
        reading += 1
    light[n]=reading

#defining a fuction to read all three pairs of sensors
def READING():                          
    for n in range(3):
        LIGHT(light_pin[n], n)
        LED(4)
        TEMP(temp_pin[n], n)
        LED(4)

#the programm
try:
    #get the info from the info-file and then modify it fittingly
    infoFile=open('/home/pi/Desktop/Tempfiles/Info.txt', 'r+')                     #opening the file
    infoLines=infoFile.readlines()                      #reading all the lines of the file
    infoData = infoLines[0].split('; ')                 #splitting the firts line into name and iteration
    infoFile.seek(0)                                    #going to position one in the file
    infoFile.truncate()                                 #deleting all that is in the file
    iteration = int(infoData[1]) + 1                    #increasing the iteration number
    if iteration < 10:                                  #adding the leading zero on numbers sub 10
        iteration = "0" + str(iteration)
    infoFile.write(infoData[0] + "; " + str(iteration)) #printing the new information to the file
    infoFile.close()                                    #closing the file 

    shutdownVar = True                                  #if the program gets to here, it will shutdown in the end

    #creating the header file
    if (int(infoData[1]) == 1):
        firstFile = open("/home/pi/Desktop/Tempfiles/" + infoData[0] + "-00-log.txt", "a")
        firstFile.write("Date Time,Temp 1,Temp 2,Temp 3,Hum 1,Hum 2,Hum 3,Light 1,Light 2,Light 3\n")
        firstFile.close()

    #creating the actual write-file
    fileName = (infoData[0] + "-" + str(infoData[1]) + "-log.txt")
    file = open("/home/pi/Desktop/Tempfiles/" + fileName, "a")                #TODO this needs to be named like the folder on the desktop of the pi, where this nees to be, also rc.local needs to be updated then
                                                                    #TODO automatically create a 00 document that contains the header of the tabel for a good time
    #main loop, do the main program x times before one shutdown and saving the 
    for rev in range(0,5):
        print(rev)
        #read three measurements of all sensors
        for r in range(0,3):                    
            READING()                       #reading all sensors
            for q in range(3):              #for each sensor, add the measurement to the collective array
                avrg_temp[q] += temp[q]          #that array saves the results of all three passes
                avrg_hum[q] += hum[q]
                avrg_light[q] += light[q]
            LED(4)                          #wait between the individual cycles
            LED(4)
            LED(4)

        #averaging out the three measurements
        for t in range(3):
            avrg_temp[t]=round(avrg_temp[t]/3, 1)
            avrg_hum[t]=round(avrg_hum[t]/300, 3)
            avrg_light[t]=avrg_light[t]/3

        #getting the time and date to write to the file
        nowTime = dt.datetime.now()
        dateTime = nowTime.strftime("%x") + " " + nowTime.strftime("%X")
        
        #writing data to the file
        file.write(dateTime + ",")
        for wn in range(0,3):                       #writing all temp measurements
            file.write(str(avrg_temp[wn]) + ",")
        for wn in range(0,3):                       #writing all hum measurements
            file.write(str(avrg_hum[wn]) + ",")
        for wn in range(0,2):                       #writing all light measurements
            file.write(str(avrg_light[wn]) + ",")
        file.write(str(avrg_light[2]) + "\n")
        
        #resetting some variables
        avrg_temp=[0,0,0]                       
        avrg_hum=[0,0,0]                        
        avrg_light=[0,0,0]                      

        #waiting in between the runs of the program with led blinking
        for wait in range(0,30):                 #TODO set the real delay time and measure how long it is in reality
            LED(10)
        print(str(rev) + " fin")

#in case the user terminated the program
except KeyboardInterrupt:
    print("\nUser terminated Programm.")

#in any case after the program is done
finally:
    file.close()                            #finally closing the file after the program is done
    GPIO.cleanup()                          #clean up the gpio configuration back to normal
    print("Program finished.")
    if shutdownVar == True:
        call("sudo reboot", shell=True)         #reboot the pi to start the program again