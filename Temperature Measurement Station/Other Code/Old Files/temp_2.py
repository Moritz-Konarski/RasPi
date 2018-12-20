#importing libraries
import time 
import smbus
import sys
from TMP102py.tmp102 import TMP102
from time import gmtime, strftime

#preparation
temp = [0,0,0]
n = 1
tmp1 = TMP102(units='C', address=0x4b, busnum=1)
#tmp2 = TMP102(units='C', address=0x4b, busnum=1)
#tmp3 = TMP102(units='C', address=0x4b, busnum=1)

#defining the function to get the temperature
def get_temp(sensor, handle, filename):
    
    #getting temperature, rounded to .1°C
    temp[sensor] = round(handle.readTemperature(),1)
    
    #printing the result to the console
    print ("temp" + str(sensor) + "= " + str(temp[sensor]) + "°C \n")
    
    #writing the result to a file
    file_log = open(file_name,'a')
    file_log.write("temp" + str(sensor) + ", " + str(temp[sensor]) + "°C, " + str(strftime("%H:%M:%S", gmtime())) + "; ")
    file_log.close()
    return

#generating the filename
file_name = ("Temp_Log " + str(strftime("%Y-%m-%d %H:%M:%S", gmtime())) + ".txt")
print (file_name) #printing the file name

#the loop
for n in range(0, 40):
    
    get_temp(sensor=1, handle=tmp1, filename=file_name)   #using the fuction to get and print the temperature

    #get_temp(sensor=2, handle=tmp2)   #using the fuction to get and print the temperature

    #get_temp(sensor=3, handle=tmp3)   #using the fuction to get and print the temperature
   
    time.sleep(float(sys.argv[1]))      #waiting for a specified amount of time