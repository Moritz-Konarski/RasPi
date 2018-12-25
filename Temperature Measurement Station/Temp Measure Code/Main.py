# from LcDisplay import lcd as lcd
from Sensor import Dht_22 as Dht_22, Light as Light
from InputOutput import InputOutput
from LED import LED

# TODO use the path object to do the info thing
# use class sensors and class arrays, do everything with parameters to make it better
#       like sensor.light.measure and so on, to make it more conscise
# make a class for reading the info.txt file to make this simpler
# make a class for the driver for the display
# look into the adafruit library to maybe make a class out of them
# with open("Info.txt", "w") as file:   use context managers

#also use "for <var> in <list>" as a for each loop to get the values
#   these are list comprehensions


# the lcd as a class
# lcd = LcDisplay.lcd()
# the getting information funtion as a class


# lcd.print_strings(string1, string2)
# lcd.clear()
# lcd.backlight
in_and_out = InputOutput()

# led = LED(in_and_out.led_pin_read())

# print(repr(in_and_out.dht_pin_read()))

# print(repr(in_and_out.light_pin_read()))

# print(repr(in_and_out.name_txt_read()))

# print(repr(in_and_out.title))

# # lcd = lcd()
# dht_obj = Dht_22(in_and_out.dht_pin_read())
light_obj = Light(in_and_out.light_pin_read())
# hum_obj = Hum([22, 13, 8, 6, 9])
# light_obj = Light([3, 1, 4, 5, 7, 8, 9, 12, 15])


# dht_obj.measure()
# print(repr(dht_obj.pins))
# print(repr(dht_obj.name_temp))
# print(repr(dht_obj.name_hum))
# print(repr(dht_obj.results))

# hum_obj.measure()
# print(repr(hum_obj.pins))
# print(repr(hum_obj.name))
# print(repr(hum_obj.hum))

light_obj.measure()
print(repr(light_obj.pins))
print(repr(light_obj.names))
print(repr(light_obj.values))
print(light_obj.values[2][1])     #can be accessed through [row][column] because it is an array