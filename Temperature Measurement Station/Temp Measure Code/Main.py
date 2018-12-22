# from LcDisplay import lcd as lcd
from Sensor import Temperature as Temp, Humidity as Hum, Light as Light
from GetInfo import InputOutput

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

inpoup = InputOutput()

print(repr(inpoup.temp_pin_read()))

# lcd = lcd()
# temp_obj = Temp([12, 23, 17, 26, 5])
# hum_obj = Hum([22, 13, 8, 6, 9])
# light_obj = Light([3, 1, 4, 5, 7, 8, 9, 12, 15])


# temp_obj.measure()
# print(repr(temp_obj.pins))
# print(repr(temp_obj.name))
# print(repr(temp_obj.temp))

# hum_obj.measure()
# print(repr(hum_obj.pins))
# print(repr(hum_obj.name))
# print(repr(hum_obj.hum))

# light_obj.measure()
# print(repr(light_obj.pins))
# print(repr(light_obj.name))
# print(repr(light_obj.light))
