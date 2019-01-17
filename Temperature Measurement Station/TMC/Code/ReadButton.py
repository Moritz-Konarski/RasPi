
# this program detects when a button is pushed and then switches on the lcd backlight
from LcDisplay import LCDisplay
import RPi.GPIO as GPIO
from time import sleep

lcd = LCDisplay()
lcd.backlight_off
pinNum = 17
ledNum = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(pinNum, GPIO.IN)
GPIO.setup(ledNum, GPIO.OUT)
GPIO.output(ledNum, GPIO.HIGH)

def switch_backlight(pinNum):
    lcd.clear
    lcd.print_strings("Hello", "World")
    print("the button is pressed")
    GPIO.output(ledNum, GPIO.HIGH)
    lcd.backlight_on
    sleep(1)
    GPIO.output(ledNum, GPIO.LOW)
    sleep(1)
    lcd.backlight_off
    GPIO.output(ledNum, GPIO.HIGH)

GPIO.add_event_detect(pinNum, GPIO.FALLING,  callback=switch_backlight, bouncetime=100)

try:
    while True:
        sleep(1)
        print("hello world")

except KeyboardInterrupt:
    print("aborted")

finally:
    GPIO.clear()
