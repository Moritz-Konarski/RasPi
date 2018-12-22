from pathlib import Path

test_folder = Path("C:/Users/morit/Desktop/test_folder")

pin_file = test_folder / "pin_numbers.txt"

info_file = test_folder / "info.txt"

track_file = test_folder / "track.txt"

log_file = test_folder / "log.txt"

class InputOutput:

    # maybe initialze this with a real funtion
    # to make it more modular

    def __init__(self):
        self.pin_file = pin_file
        self.info_file = info_file
        self.track_file = track_file
        self.log_file = log_file

    def temp_pin_read(self):
        with open(self.pin_file, "r+") as file:
            read = file.readline()
        string = read.split(" ")
        result = [int(number) for number in string]
        return result
    
    def info_txt_read(self):
        # read info from Info.txt
        self.temp_pins=- 0
        self.hum_pins = 0
        self.light_pins = 0

    def track_txt_write(self, iteration):
        pass

    def track_txt_red(self):
        pass

    def log_txt_write(self, string):
        pass   