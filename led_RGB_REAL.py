from gpiozero import LED
from gpiozero import PWMLED
import time

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

# Raspberry Pi Pins
redL = PWMLED(6) 
greenL = PWMLED(5) 
blueL = PWMLED(0)
redR = PWMLED(26)
greenR = PWMLED(19)
blueR = PWMLED(13)

def parse(d):
    for key, value in d.items():
        if isinstance(value,dict):
            yield from parse(value)
        else:
            yield key,value
            
def eyes_RGB(eyes_status):
    if debug_messages : print("Running eyes_RGB function")
    if debug_messages : print(eyes_status)
    left,right = eyes_status
    red,green,blue = left
    red2,green2,blue2 = right
    redL.value = eyes_status[0][red]
    greenL.value = eyes_status[0][green]
    blueL.value = eyes_status[0][blue]
    redR.value = eyes_status[1][red2]
    greenR.value = eyes_status[1][green2]
    blueR.value = eyes_status[1][blue2]

def main():
    while True:
        print("Welcome To The Makey Bot")
        eyes_RGBLEDs = [{'redL':0, 'greenL':0, 'blueL':0}, {'redR':0, 'greenR':0, 'blueR':0}]
        print("left eye:")
        redL_status = float(input("red: ")) #gets user input for LED value (0 to 1)
        greenL_status = float(input("green: "))
        blueL_status = float(input("blue: "))
        print("right eye:")
        redR_status = float(input("red: ")) #gets user input for LED value (0 to 1)
        greenR_status = float(input("green: "))
        blueR_status = float(input("blue: "))
        eyes_RGBLEDs[0]["redL"] = redL_status #changes the value in the dictionary
        eyes_RGBLEDs[0]["greenL"] = greenL_status
        eyes_RGBLEDs[0]["blueL"] = blueL_status
        eyes_RGBLEDs[1]["redR"] = redR_status
        eyes_RGBLEDs[1]["greenR"] = greenR_status
        eyes_RGBLEDs[1]["blueR"] = blueR_status
        print(eyes_RGBLEDs)
        
        if debug_messages : print("Calling eyes_RGB function")
        eyes_RGB(eyes_RGBLEDs)
        if debug_messages : print("Returned from eyes_RGB function")
main()
