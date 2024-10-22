#Importing modules and classes
import tm1637
import time
import numpy as np
from datetime import datetime
from gpiozero import CPUTemperature

#Creating 4-digit 7-segment diplay object
tm = tm1637.TM1637(clk=18, dio=23) #Using GPIO pins
clear = [0, 0, 0, 0] #Defining values used to clear

#Get input from user
name = input("Enter name: ")

#Displaying "Hello Name" in display
tm.write(clear)
time.sleep(1)
s = 'Hello '
tm.scroll(s, delay=250)
tm.scroll(name, delay=250)
time.sleep(2)
