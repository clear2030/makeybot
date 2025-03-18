from gpiozero import LED
import time

red_LED = LED(3) #sets LEDs to pins
yellow_LED = LED(27)
green_LED = LED(10)
traffic_light = {"red_LED":0, "yellow_LED":0, "green_LED":0} #creates dictionary

def stop_light(var): #function that turns the LEDs on and off
    if traffic_light[var] == 0:
        eval(var + ".off()") #uses eval function to turn strings into python commmands
    else:
        eval(var + ".on()")
    
def main():
    print("Welcome to the Makey Bot")
    red_status = int(input("red: ")) #gets user input for LED value (0 or 1)
    yellow_status = int(input("yellow: "))
    green_status = int(input("green: "))
    traffic_light["red_LED"] = red_status #changes the value in the dictionary
    traffic_light["yellow_LED"] = yellow_status
    traffic_light["green_LED"] = green_status
    print(traffic_light)
    stop_light("red_LED") #calls the function to turn on/off the LED
    stop_light("yellow_LED")
    stop_light("green_LED")
    
main()

# GitHub: https://github.com/clear2030/Assignments/blob/main/MakeyBot_Stop_Light.py
# Hacker: Nathan Lien  
# This example code is licensed under the CC BY-NC-SA 4.0, GNU GPL and EUPL
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.gnu.org/licenses/gpl-3.0.en.html
# https://eupl.eu/
# Program/Design Name: MakeyBot_Stop_Light.py
# Description:    This is a program to control (turn on/off) a set of 3 LEDs that takes user input and uses functions, 
# that can be called with external parameters.
# program description:
# 1) Gets user input for the LED status (either 1 or 0)
# 2) Change those values in the dictionary
# 3) The function will take those values from the dictionary and turn on/off the corresponding LEDs
# Dependencies:   python3
#   Inputs: either 1 or 0 for each LED to indicate if it should be on or off
#   Outputs: the LEDs turn on or off
