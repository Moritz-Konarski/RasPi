import os
import re
from time import sleep

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")
for i in range(12):

    print(i)

    with open("/sys/bus/w1/devices/28-021318edc3aa/w1_slave", "r") as file:
        read = file.readlines()

    while "NO\n" in read[0]:
        sleep(.5)
        with open("/sys/bus/w1/devices/28-021318edc3aa/w1_slave", "r") as file:
            read = file.readlines()

    for read_line in read:
        if "t=" in read_line:
            nums = [float(s) for s in re.findall(r'-?\d+\.?\d*', read_line)]
            temp = round(nums[-1] / 100) / 10

    print(temp)
