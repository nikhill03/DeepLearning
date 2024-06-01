from datetime import datetime
import time

def turn_on_light():
    print("Turning on the light")

def turn_off_light():
    print("Turning off the light")


if __name__ == "__main__":
    isPresent = int(input("Is Person Present (0/1) : "))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    if("06:00:00" <= current_time <= "22:00:00"):
        time = "morning"
    else:
        time = "night"
    
    print("Current Time : " + time)
    
    if not isPresent:
        turn_off_light()
    elif time=="morning":
        turn_on_light()
    else:
        turn_off_light()
