#!/usr/bin/python
# importing libraries-----------------------------------------------------------------------------------------
import sys, os, Adafruit_DHT
from time import sleep
import datetime as dt
from subprocess import call
import RPi.GPIO as GPIO
import lcddriver
from time import *
# import FunHouse from JustForFun

# temp_1.addSensor("Temperature", 27)


lcd = lcddriver.lcd()
lcd.lcd_clear()

# defining pin connections------------------------------------------------------------------------------------
led_pin = 23  # pin of the LED
temp_pin = [22, 27, 17]  # pins of the temp sensors
light_pin = [18, 15, 14]  # pins of the light sensors

# setting gpio modes------------------------------------------------------------------------------------------
GPIO.setmode(GPIO.BCM)  # setting GPIO mode to chip-designations
GPIO.setup(led_pin, GPIO.OUT)  # setting the LED pin to output


# TODO use the path object to do the info thing
# use class sensors and class arrays, do everything with parameters to make it better
#       like sensor.light.measure and so on, to make it more conscise
# make a class for reading the info.txt file to make this simpler
# make a class for the driver for the display
# look into the adafruit library to maybe make a class out of them
# with open("Info.txt", "w") as file:   use context managers

#also use "for <var> in <list>" as a for each loop to get the values
#   these are list comprehensions



# defining variables------------------------------------------------------------------------------------------
temp = [0, 0, 0]  # temp measurements
hum = [0, 0, 0]  # humidity measurements
light = [0, 0, 0]  # light measuremenss
sum_temp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # sum of three measurement passes for temp
sum_hum = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # sum of three measurement passes for humindity
sum_light = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # sum of three measurement passes for light
avrg_temp = [0, 0, 0]  # average of three temp passes
avrg_hum = [0, 0, 0]  # average of three humidity passes
avrg_light = [0, 0, 0]  # average of three light passes
shutdownVar = False
maxrev = 113


# defining LED function---------------------------------------------------------------------------------------
def led(interval):
    sleep(interval / 2)
    GPIO.output(23, 1)  # on
    sleep(.5)
    GPIO.output(23, 0)  # off
    sleep(interval / 2)

# defining temp/humidity measurement function-----------------------------------------------------------------
def temp(pin, n):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    if humidity is None and temperature is None:
        temp[n] = '--No Data--'
        hum[n] = '--No Data--'
    else:
        temp[n] = round(temperature * 10) / 10
        hum[n] = round(humidity * 10) / 10


# defining light measurement function-------------------------------------------------------------------------
def light(pin, n):
    value = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW and value < 100000):
        value += 1
    light[n] = value


# defining a fuction to read all three pairs of sensors-------------------------------------------------------
def reading():
    for n in range(3):
        light(light_pin[n], n)
        led(4)
        temp(temp_pin[n], n)
        led(4)


# defining a function to print to the lcd display-------------------------------------------------------------
def lcdPrint(string1, string2):
    lcd.lcd_clear()
    lcd.lcd_display_string(str(string1), 1)
    lcd.lcd_display_string(str(string2), 2)


# the programm------------------------------------------------------------------------------------------------
try:
    lcd.lcd_backlight("on")
    sleep(2)
    lcdPrint("Program Starts", "Setting Up")
    sleep(2)
    # get the info from the info-file and then modify it fittingly--------------------------------------------
    infoFile = open('/home/pi/Desktop/Info.txt', 'r+')  # opening the file
    infoLines = infoFile.readlines()  # reading all the lines of the file
    infoData = infoLines[0].split('; ')  # splitting the firts line into name and iteration
    infoFile.seek(0)  # going to position one in the file
    infoFile.truncate()  # deleting all that is in the file
    iteration = int(infoData[1]) + 1  # increasing the iteration number
    writeIteration = iteration - 1
    if iteration < 10:  # adding the leading zero on numbers sub 10
        iteration = "0" + str(iteration)
    infoFile.write(infoData[0] + "; " + str(iteration))  # printing the new information to the file
    infoFile.close()  # closing the file
    lcdPrint("Iteration Nr.:", str(writeIteration))
    sleep(5)

    shutdownVar = True  # if the program gets to here, it will shutdown in the end

    # creating the header file--------------------------------------------------------------------------------
    if (int(infoData[1]) == 1):
        firstFile = open("/home/pi/Desktop/Tempfiles/" + infoData[0] + "-00-log.txt", "a")
        firstFile.write("Date Time,Temp 1,Temp 2,Temp 3,Hum 1,Hum 2,Hum 3,Light 1,Light 2,Light 3\n")
        firstFile.close()

    # creating the actual write-file-name---------------------------------------------------------------------
    if (writeIteration < 10):
        fileName = (infoData[0] + "-0" + str(writeIteration))
    else:
        fileName = (infoData[0] + "-" + str(writeIteration))

    # main loop, do the main program x times before one shutdown and saving the-------------------------------
    for rev in range(0, maxrev):

        lcdPrint("Measuring ...", "")
        # read three measurements of all sensors--------------------------------------------------------------
        for r in range(0, 3):
            reading()  # reading all sensors
            for q in range(3):  # for each sensor, add the measurement to the collective array
                avrg_temp[q] += temp[q]  # that array saves the results of all three passes
                avrg_hum[q] += hum[q]
                avrg_light[q] += light[q]
            led(4)  # wait between the individual cycles
            led(4)
            led(4)

        lcdPrint("Measuring", "Complete")
        sleep(2)

        # averaging out the three measurements----------------------------------------------------------------
        for t in range(3):
            avrg_temp[t] = round(avrg_temp[t] / 3, 1)
            avrg_hum[t] = round(avrg_hum[t] / 300, 3)
            avrg_light[t] = avrg_light[t] / 3

        tempstring = (str(avrg_temp[0]) + "  " + str(avrg_temp[1]) + "  " + str(avrg_temp[2]))
        humstring = (str(avrg_hum[0] * 100) + "  " + str(avrg_hum[1] * 100) + "  " + str(avrg_hum[2] * 100))
        # lcdPrint(tempstring, humstring)

        # getting the time and date to write to the file------------------------------------------------------
        nowTime = dt.datetime.now()
        dateTime = nowTime.strftime("%x") + " " + nowTime.strftime("%X")

        file = open("/home/pi/Desktop/Tempfiles/" + fileName + "-log.txt", "a")
        # writing data to the file----------------------------------------------------------------------------
        file.write(dateTime + ",")
        for wn in range(0, 3):  # writing all temp measurements
            file.write(str(avrg_temp[wn]) + ",")
        for wn in range(0, 3):  # writing all hum measurements
            file.write(str(avrg_hum[wn]) + ",")
        for wn in range(0, 2):  # writing all light measurements
            file.write(str(avrg_light[wn]) + ",")
        file.write(str(avrg_light[2]) + "\n")
        file.close()
        # resetting some variables
        avrg_temp = [0, 0, 0]
        avrg_hum = [0, 0, 0]
        avrg_light = [0, 0, 0]

        # waiting in between the runs of the program with led blinking and displaying the time and temp-------
        for n in range(20):
            nowTime = dt.datetime.now()
            timeString = (nowTime.strftime("%a") + " " + nowTime.strftime("%r"))
            iterationString = (str(20 - n) + "/" + str(20) + "  -" + str((20 - n) * 30) + "s")
            lcdPrint(timeString, iterationString)
            led(10)
            lcdPrint(tempstring, humstring)
            led(10)
            led(10)

# in case the user terminated the program---------------------------------------------------------------------
except KeyboardInterrupt:
    lcdPrint("Program", "Terminated")
    sleep(3)

# in any case after the program is done-----------------------------------------------------------------------
finally:
    GPIO.cleanup()  # clean up the gpio configuration back to normal
    lcdPrint("Finished!", "")
    sleep(3)
    lcd.lcd_clear()
    lcd.lcd_backlight("off")
    if shutdownVar == True:
        # file.close()                               #finally closing the file after the program is done
        lcdPrint("Rebooting Now", "")
        sleep(3)
        lcd.lcd_clear()
        lcd.lcd_backlight("off")
        call("sudo reboot", shell=True)  # reboot the pi to start the program again
