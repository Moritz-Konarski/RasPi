class Sensor:
	def __init__(self, pin, name):
		self.pin = pin
		self.name = name

class Temperature(Sensor):
	def __init__(self, pin, name, number):
		super().__init__(pin, name)
		self.number = number
	
temp_1 = Temperature(27, 'Temp 1', 1)

# print(temp_1.pin)
# print(temp_1.name)
# print(temp_1.number)