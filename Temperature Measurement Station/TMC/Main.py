#!/usr/bin/python
import RPi.GPIO as GPIO
from LcDisplay import LCDisplay
from Sensor import Dht22, Light, OutdoorTemp
from InputOutput import InputOutput
from time import sleep
from LED import LEDIndicator

MEASURE_INTERVAL = 2                                        # interval in minutes
PAUSE = 2                                                   # pause between individual measurements
ITERATIONS_PER_DAY = int(24 * 60 / MEASURE_INTERVAL)        # iterations per day
BLINKS_OF_LED = 30 * MEASURE_INTERVAL                       # number of LED blinks to fill the interval
SECONDS = BLINKS_OF_LED * 2                                 # seconds that the interval is equal to

try:
    input_output = InputOutput()

    # lcd = LCDisplay()

    # lcd.backlight_on

    dht_sensor = Dht22(input_output.dht_pins)

    # light_obj = Light(input_output.light_pins)

    out_temp_sensor = OutdoorTemp(input_output.out_temp_addr)

    led_indicator = LEDIndicator(input_output.led_pins)
#------------------------------------------------------------------------------------------
    input_output.title_read()

    input_output.track_init()

    input_output.log_init(dht_sensor.names, out_temp_sensor.names, )

    led_indicator.blink(PAUSE)

    while True:

        input_output.track_read()

        for i in range(ITERATIONS_PER_DAY):

            led_indicator.on
            
            dht_sensor.measure()
            
            led_indicator.blink(PAUSE)

            led_indicator.on

            out_temp_sensor.measure()

            led_indicator.blink(PAUSE)

            # light_obj.measure()
            
            input_output.log_write(dht_sensor.values, out_temp_sensor.values, )
            
            led_indicator.blink(BLINKS_OF_LED)

except KeyboardInterrupt:
    print("\nUser terminated program. Shutting down.")
    led_indicator.blink()

except IOError as error:
    print("--------------------SOMETHING WENT WRONG--------------------")
    print(error.args)
    led_indicator.blink()

finally:
    # lcd.backlight_off
    # lcd.clear
    GPIO.cleanup()