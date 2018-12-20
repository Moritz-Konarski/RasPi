import lcddriver
from time import *
import datetime as dt
from subprocess import call
import RPi.GPIO as GPIO
pin2 = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin2, GPIO.OUT)
sleep(1)
GPIO.output(pin2, 0)
sleep(5)
 
lcd = lcddriver.lcd()
maxrev = 5

def LcdPrint(string1, string2):
    lcd.lcd_clear()
    lcd.lcd_display_string(str(string1), 1)
    lcd.lcd_display_string(str(string2), 2)

lcd.lcd_clear()
lcd.lcd_backlight("ON")

for n in range(maxrev):
    nowTime = dt.datetime.now()
    timeString = (nowTime.strftime("%a") + " " + nowTime.strftime("%r"))
    interationString = (str(maxrev - n) + "/" + str(maxrev) + "  -" + str((maxrev - n)*30) + "s")
    LcdPrint(timeString, interationString)
    sleep(5)
    LcdPrint("23,4  23,5  23,9", "45,6  47,3  42,7")
    sleep(5)

LcdPrint("Shutting", "Down")
sleep(3)
lcd.lcd_backlight("OFF")
lcd.lcd_clear()
GPIO.output(pin2, 1)
GPIO.cleanup()
