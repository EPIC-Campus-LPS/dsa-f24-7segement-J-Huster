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
#Clear the display
tm.write(clear)
#Pause the program for one second
time.sleep(1)
#Assign the word Hello to the variable s
s = 'Hello '
#Scroll the word Hello across the display
tm.scroll(s, delay=250)
#Scroll the user input name across the display
tm.scroll(name, delay=250)
#Pause the program for two seconds
time.sleep(2)
