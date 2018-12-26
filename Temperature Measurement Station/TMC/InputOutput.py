"""
Desktop on Pi:
/home/pi/Desktop
Folder in file struture:
/home/pi/<folder name>
"""

from pathlib import Path

test_folder = Path("C:/Users/morit/Desktop/test_folder")

pin_file = test_folder / "pin_numbers.txt"

name_file = test_folder / "name.txt"

track_file = test_folder / "track.txt"

log_file = test_folder / "log.txt"

#TODO make this whole thing an array to make it shorter because it is literally five times the same code

dht_signifier = "DHT22: "
light_signifier = "Light: "
name_signifier = "Name: "
led_signifier = "LED: "
title = "not_given"

class InputOutput:

    # maybe initialze this with a real funtion
    # to make it more modular

    def __init__(self):
        self.pin_file = pin_file
        self.name_file = name_file
        self.track_file = track_file
        self.log_file = log_file

    def dht_pin_read(self):        
        with open(self.pin_file, "r") as file:
            while (True):
                read = file.readline()
                if read.startswith(dht_signifier):
                    read = read.replace(dht_signifier, "")
                    read = read.split(" ")
                    dht_pins = [int(number) for number in read]
                    return dht_pins
                elif read is "":
                    print ("There are no DHT22 pins.")
                    break

    def light_pin_read(self):        
        with open(self.pin_file, "r") as file:
            while (True):
                read = file.readline()
                if read.startswith(light_signifier):
                    read = read.replace(light_signifier, "")
                    read = read.split(" ")
                    light_pins = [int(number) for number in read]
                    return light_pins
                elif read is "":
                    print ("There are no Light pins.")
                    break
    
    def name_txt_read(self):        
        with open(self.name_file, "r") as file:
            while (True):
                read = file.readline()
                if read.startswith(name_signifier):
                    read = read.replace(name_signifier, "")
                    self.title = read
                    return read
                elif read is "":
                    print ("There is no name here.")
                    break

    def led_pin_read(self):        
        with open(self.name_file, "r") as file:
            while (True):
                read = file.readline()
                if read.startswith(led_signifier):
                    read = read.replace(led_signifier, "")
                    led_pin = int(read)
                    return led_pin
                elif read is "":
                    print ("There is no led pin here.")
                    break

    def track_txt_write(self, iteration):
        pass

    def track_txt_read(self):
        pass

    def log_txt_write(self, temp_hum_values=[][], light_values=[][]):

        date_string = ""
        temp_string = temp_string.append("{};".format(temp_hum_values[0][n]))
        hum_string = ""
        light_string = ""

        total_string = (date_string + temp_string + hum_string + light_string + "\n")
        with open(log_file, "a") as file:
            file.write(total_string)

           