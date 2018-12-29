#!/usr/bin/python
import LcDisplay
import RPi.GPIO as GPIO
from Sensor import Dht_22, Light, TempOut
from InputOutput import I_O
from time import sleep
from LED import LED

INTERVAL = 4                                        # interval in minutes
ITERATIONS_PER_DAY = int(24 * 60 / INTERVAL)        # for 6 its 240
BLINKS_OF_LED = 30 * INTERVAL                       # number of LED blinks to fill the interval
SECONDS = BLINKS_OF_LED * 2                         # seconds that the interval is equal to

i_o = I_O()
# lcd = LcDisplay.lcd()
# lcd.backlight('on')
dht_obj = Dht_22(i_o.dht_pin_read())
# light_obj = Light(i_o.light_pin_read())
temp_out_obj = TempOut(i_o.temp_out_address_read())
# led_obj = LED(i_o.led_pin_read())

i_o.name_txt_read()
i_o.track_txt_prime()
i_o.log_txt_prime(dht_obj.temp_hum_names, temp_out_obj.names, [])
sleep(4)

while True:

    i_o.track_txt_read()

    for i in range(1, 50): # ITERATIONS_PER_DAY):
        
        dht_obj.measure()
        
        temp_out_obj.measure()

        # light_obj.measure()
        
        i_o.log_txt_write(dht_obj.temp_hum_values, temp_out_obj.values, [])
        
        sleep(30) # SECONDS)
    
# lcd.backlight('Off')
# lcd.clear()

GPIO.cleanup()