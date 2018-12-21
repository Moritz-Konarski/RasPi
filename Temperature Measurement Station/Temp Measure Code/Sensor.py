"""
Relevant funtions:

"""


class Temperature:

    def __init__(self, pins=[]):
        self.pins = pins
        self.name = ["Temp {}".format(n + 1) for n in range(len(pins))]
    
    def measure(self):
        self.temp = [pin*pin for pin in self.pins]# to be determined


class Humidity:

    def __init__(self, pins=[]):
        self.pins = pins
        self.name = ["Hum {}".format(n + 1) for n in range(len(pins))]
    
    def measure(self):
        self.hum = [pin*pin for pin in self.pins]# to be determined

class Light:

    def __init__(self, pins=[]):
        self.pins = pins
        self.name = ["Light {}".format(n + 1) for n in range(len(pins))]
    
    def measure(self):
        self.light = [pin*pin for pin in self.pins]# to be determined