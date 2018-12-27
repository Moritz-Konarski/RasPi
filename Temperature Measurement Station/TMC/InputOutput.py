"""
Desktop on Pi:
/home/pi/Desktop
Folder in file struture:
/home/pi/<folder name>
"""
import os
from pathlib import Path
import datetime as dt

info_path = Path("/home/pi/Desktop/Program/Info")
user_path = Path("/home/pi/Desktop/User")

pin_file = info_path / "pin_numbers.txt"
name_file = user_path / "name.txt"

led_signifier = "LED: "
dht_signifier = "DHT22: "
name_signifier = "Name: "
light_signifier = "Light: "
track_signifier = "Iteration: "

class I_O:

    def __init__(self):
        self.pin_file = pin_file
        self.name_file = name_file
        self.iteration = 0

    def dht_pin_read(self):        
        with self.pin_file.open() as file:
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
        with self.pin_file.open() as file:
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

    def led_pin_read(self):        
        with self.pin_file.open() as file:
            while (True):
                read = file.readline()
                if read.startswith(led_signifier):
                    read = read.replace(led_signifier, "")
                    led_pin = int(read)
                    return led_pin
                elif read is "":
                    print ("There is no led pin here.")
                    break
    
    def name_txt_read(self):        
        with self.name_file.open() as file:
            while (True):
                read = file.readline()
                if read.startswith(name_signifier):
                    read = read.replace(name_signifier, "")
                    self.title = read
                    log_dir_name = "{} Logs".format(self.title)
                    self.log_dir = user_path / log_dir_name
                    log_file_name = "{}_{:03}_log.txt".format(self.title, self.iteration)
                    self.log_file = self.log_dir / log_file_name
                    if self.log_dir.exists() is False:
                        self.log_dir.mkdir()                
                    break
                elif read is "":
                    print ("There is no name here.")
                    break
    
    def track_txt_read(self):
        with self.track_file.open("r") as file:
            while (True):
                read = file.readline()
                if read.startswith(track_signifier):
                    read = read.replace(track_signifier, "")
                    iteration = int(read)
                    self.iteration = iteration + 1
                    break
                elif read is "":
                    print ("There is no track number here here.")
                    break
        log_file_name = "{}_{:03}_log.txt".format(self.title, self.iteration)
        self.log_file = self.log_dir / log_file_name
        track_file_content = "{}{}".format(track_signifier, self.iteration)
        with self.track_file.open("w") as file:
            file.write(track_file_content.decode('utf-8'))

    def track_txt_prime(self):
        track_file_name = "{}_track.txt".format(self.title)
        self.track_file = info_path / track_file_name
        track_file_content = "{}{}".format(track_signifier, "0")
        with self.track_file.open("w") as file:
            file.write(track_file_content.decode('utf-8'))

    def log_txt_prime(self, dht_names=[[]], light_names=[]):
        string = []
        string.append("{}".format("Time"))
        for name in dht_names:
            string.append("{}".format(name[0]))
        for name in dht_names:
            string.append("{}".format(name[1]))
        for name in light_names:
            string.append("{}".format(name))
        string.append("\n")
        self.title_string = ', '.join(string)
        print(self.title_string)
        with self.log_file.open("a") as file:
            file.write(self.title_string.decode('utf-8'))

    def log_txt_write(self, temp_hum_values=[[]], light_values=[]):
        string = []
        dateTime = dt.datetime.now().strftime("%x") + " " + dt.datetime.now().strftime("%X")
        string.append(dateTime)
        for value in temp_hum_values:
            string.append("{}".format(value[0]))
        for value in temp_hum_values:
            string.append("{}".format(value[1] / 100))
        for value in light_values:
            string.append("{}".format(value))
        string.append("\n")
        self.log_string = ', '.join(string)
        print(self.log_string)
        with self.log_file.open("a") as file:
            file.write(self.log_string.decode('utf-8'))