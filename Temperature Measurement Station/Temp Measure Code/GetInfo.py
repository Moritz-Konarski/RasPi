class InputOutput:

    # maybe initialze this with a real funtion
    # to make it more modular

    info_path = "a"
    info_file_name = "b"

    track_path = ""
    track_file_name = ""

    log_path = ""
    log_file_name = ""

    def __init__(self, info_path, info_file_name):
        self.info_path = info_path
        self.info_file_name = info_file_name
    
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