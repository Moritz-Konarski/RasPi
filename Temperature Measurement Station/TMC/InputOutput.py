"""
Desktop on Pi:
/home/pi/Desktop
Folder in file struture:
/home/pi/<folder name>
"""

from pathlib import Path
import datetime as dt

info_path = Path("/home/pi/Desktop/Info")

pin_file = info_path / "pin_numbers.txt"
name_file = info_path / "name.txt"
track_file = info_path / "track.txt"

title = "not_given"
led_signifier = "LED: "
dht_signifier = "DHT22: "
name_signifier = "Name: "
light_signifier = "Light: "

class I_O:

    def __init__(self):
        self.pin_file = pin_file
        self.name_file = name_file
        self.track_file = track_file

    def __str__(self):
        pass

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
                    log_file_name = "{}_log.txt".format(self.title)
                    self.log_file = info_path / log_file_name
                    return read
                elif read is "":
                    print ("There is no name here.")
                    break

    def track_txt_write(self, iteration):
        pass

    def track_txt_read(self):
        pass

    def log_txt_prime(self, dht_names=[[]], light_names=[]):
        string = []
        string.append("{:17}".format("Time"))
        for name in dht_names:
            string.append("{:5}".format(name[0]))
        for name in dht_names:
            string.append("{:5}".format(name[1]))
        for name in light_names:
            string.append("{:6}".format(name))
        string.append("\n")
        self.title_string = ', '.join(string)
        # print(self.title_string)
        with self.log_file.open("a") as file:
            file.write(self.title_string.decode('utf-8'))

    def log_txt_write(self, temp_hum_values=[[]], light_values=[]):
        string = []
        dateTime = dt.datetime.now().strftime("%x") + " " + dt.datetime.now().strftime("%X")
        string.append(dateTime)
        for value in temp_hum_values:
            string.append("{:5.1f}".format(value[0]))
        for value in temp_hum_values:
            string.append("{:05.3f}".format(value[1] / 100))
        for value in light_values:
            string.append("{:6}".format(value))
        string.append("\n")
        self.log_string = ', '.join(string)
        # print(self.log_string)
        with self.log_file.open("a") as file:
            file.write(self.log_string.decode('utf-8'))