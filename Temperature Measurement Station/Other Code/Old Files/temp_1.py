#importing libraries
import time 
import smbus
import sys
from TMP102py.tmp102 import TMP102

#preparation
temp = [0,0,0,0]
n = 1
bus = smbus.SMBus(1)
tmp1 = TMP102(units='C', address=0x4b, busnum=1)

#defining the function to get the temperature
def get_temp( address, sensor):
    temp[sensor] = bus.read_byte_data(address, 0x00)
    print ("temp" + str(sensor) + "= " + str(temp[sensor]) + "°C \n")
    file_log = open('temp1_test.txt','w')
    file_log.write("temp" + str(sensor) + ", " + str(temp[sensor]) + "°C; \n")
    file_log.close()
    return

#the loop
for n in range(0, 40):
    
    #get_temp( address=0x4b, sensor=1)   #using the fuction to get and print the temperature
    x=tmp1.readTemperature()
    print str(x)
    time.sleep(float(sys.argv[1]))      #waiting for a specified amount of time
