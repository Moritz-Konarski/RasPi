#!/usr/bin/python
import LcDisplay
import RPi.GPIO as GPIO
from Sensor import Dht_22, Light, TempOut
from InputOutput import I_O
from time import sleep
from LED import LED

INTERVAL = 2                                        # interval in minutes
ITERATIONS_PER_DAY = int(24 * 60 / INTERVAL)        # iterations per day
BLINKS_OF_LED = 30 * INTERVAL                       # number of LED blinks to fill the interval
SECONDS = BLINKS_OF_LED * 2                         # seconds that the interval is equal to

try:
    i_o = I_O()
    # lcd = LcDisplay.lcd()
    # lcd.backlight('on')
    dht_obj = Dht_22(i_o.dht_pin_read())
    # light_obj = Light(i_o.light_pin_read())
    temp_out_obj = TempOut(i_o.temp_out_address_read())
    led_obj = LED(i_o.led_pin_read())

    i_o.name_txt_read()

    i_o.track_txt_prime()

    i_o.log_txt_prime(dht_obj.temp_hum_names, temp_out_obj.names, [])

    led_obj.blink(3)

    while True:

        i_o.track_txt_read()

        for i in range(1, ITERATIONS_PER_DAY):

            led_obj.on()
            
            dht_obj.measure()
            
            led_obj.blink(2)

            led_obj.on()

            temp_out_obj.measure()

            led_obj.blink(2)

            # light_obj.measure()
            
            i_o.log_txt_write(dht_obj.temp_hum_values, temp_out_obj.values, [])
            
            led_obj.blink(BLINKS_OF_LED)

            # sleep(30) # SECONDS)

except KeyboardInterrupt:
    print("\nUser terminated program. Shutting down.")
    led_obj.blink(1)

except IOError as error:
    print("--------------------SOMETHING WENT WRONG--------------------")
    print(error.args)
    # raise

finally:
    # lcd.backlight('Off')
    # lcd.clear()
    GPIO.cleanup()