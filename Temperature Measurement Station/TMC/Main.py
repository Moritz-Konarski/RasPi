import LcDisplay
from Sensor import Dht_22, Light
from InputOutput import I_O
from LED import LED
import RPi.GPIO as GPIO
from time import sleep

# one blink takes 2 seconds
blinks = 10

"""Initialization"""
# io object
i_o = I_O()

# lcd object
# lcd = LcDisplay.lcd()
# lcd.backlight('on')

# temp and humidity sensor object
dht_obj = Dht_22(i_o.dht_pin_read())

# light sensor object
light_obj = Light(i_o.light_pin_read())

# led object
# led_obj = LED(i_o.led_pin_read())

"""Actual Code"""
title = i_o.name_txt_read()
# print(title)
i_o.log_txt_prime(dht_obj.temp_hum_names, light_obj.names)
# lcd.print_strings(title,"")
sleep(4)
# led_obj.blink(2)
for i in range(132):
    # num = "------{:04}------".format(i)
    # print(num)   
    # lcd.print_strings(num,"")
    # sleep(4)
    # led_obj.blink(3)

    # measuring temp and hum and printing results
    dht_obj.measure()
    # print(repr(dht_obj.pins))
    # print(repr(dht_obj.temp_hum_names))
    # print(repr(dht_obj.temp_hum_values))

    # lcd.print_strings(dht_obj.temp_hum_names, str(dht_obj.temp_hum_values))
    # sleep(4)
    
    # led_obj.blink(3)

    # measuring light
    light_obj.measure()
    # print(repr(light_obj.pins))
    # print(repr(light_obj.names))
    # print(repr(light_obj.values))


    i_o.log_txt_write(dht_obj.temp_hum_values, light_obj.values)
    # blinking ten times
    sleep(300)
    # led_obj.blink(blinks)

# lcd.backlight('Off')
# lcd.clear()
# finally
GPIO.cleanup()