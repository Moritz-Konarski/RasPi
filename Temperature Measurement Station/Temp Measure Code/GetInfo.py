from pathlib import Path

test_folder = Path("C:/Users/morit/Desktop/test_folder")

pin_file = test_folder / "pin_numbers.txt"

name_file = test_folder / "name.txt"

track_file = test_folder / "track.txt"

log_file = test_folder / "log.txt"

class InputOutput:

    # maybe initialze this with a real funtion
    # to make it more modular

    def __init__(self):
        self.pin_file = pin_file
        self.name_file = name_file
        self.track_file = track_file
        self.log_file = log_file
        self.dht_signifier = "DHT22: "
        self.light_signifier = "Light: "
        self.name_signifier = "Name: "
        self.led_signifier = "LED: "
        self.title = "not_given"

    def dht_pin_read(self):        
        with open(self.pin_file, "r") as file:
            while (True):
                read = file.readline()
                if read.startswith(self.dht_signifier):
                    read = read.replace(self.dht_signifier, "")
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
                if read.startswith(self.light_signifier):
                    read = read.replace(self.light_signifier, "")
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
                if read.startswith(self.name_signifier):
                    read = read.replace(self.name_signifier, "")
                    self.title = read
                    return read
                elif read is "":
                    print ("There is no name here.")
                    break

    def led_pin_read(self):        
        with open(self.name_file, "r") as file:
            while (True):
                read = file.readline()
                if read.startswith(self.led_signifier):
                    read = read.replace(self.led_signifier, "")
                    led_pin = int(read)
                    return led_pin
                elif read is "":
                    print ("There is no led pin here.")
                    break

    def track_txt_write(self, iteration):
        pass

    def track_txt_read(self):
        pass

    def log_txt_write(self, string):
        pass   