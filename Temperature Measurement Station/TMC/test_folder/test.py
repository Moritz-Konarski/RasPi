#!/usr/bin/python
import RPi.GPIO as GPIO
from LcDisplay import LCDisplay
from Sensor import Dht22, Light, OutdoorTemp
from InputOutput import InputOutput
from time import sleep
from LED import LEDIndicator

try:
    input_output = InputOutput()

    lcd = LCDisplay()

    lcd.backlight_on

    lcd.print_strings("Hello you", "cruel")

    dht_sensor = Dht22(input_output.dht_pins)

    light_sensor = Light(input_output.light_pins)

    out_temp_sensor = OutdoorTemp(input_output.out_temp_addr)

    led_indicator = LEDIndicator(input_output.led_pins)
    
    input_output.title_read()       # the program gets to here, then crashes
    # problem is from here on down 
    input_output.track_init()

    input_output.log_init(dht_sensor.names, out_temp_sensor.names, light_sensor.names)

    led_indicator.blink(3)

    lcd.backlight_off

    led_indicator.blink(3)

    lcd.backlight_on

    input_output.track_read()

    for i in range(2):

        led_indicator.on

        lcd.print_strings("measuring", "temps")
        
        dht_sensor.measure()
        
        led_indicator.blink(3)

        led_indicator.on

        out_temp_sensor.measure()

        led_indicator.blink(3)

        light_sensor.measure()
        
        input_output.log_write(dht_sensor.values, out_temp_sensor.values, light_sensor.values)

        lcd.print_strings("waiting", "for next time")
        
        led_indicator.blink(10)

except KeyboardInterrupt:
    print("\nUser terminated program. Shutting down.")
    led_indicator.blink()

except IOError as error:
    print("--------------------SOMETHING WENT WRONG--------------------")
    print(error.args)
    led_indicator.blink()

finally:
    GPIO.cleanup()
    lcd.clear
    lcd.backlight_off