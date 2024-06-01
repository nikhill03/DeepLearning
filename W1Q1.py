from datetime import datetime

# Format: Location : {Preference: {Time: _______ }}
rulebase = {
    'cold': {
        'cold': {
            'morning': 0,
            'evening': 0,
            'night': 0
        },
        'warm': {
            'morning': 2,
            'evening': 1,
            'night': 3
        },
        'hot': {
            'morning': 5,
            'evening': 4,
            'night': 4
        },
    },
    'warm': {
        'cold': {
            'morning': -2,
            'evening': -1,
            'night': -2
        },
        'warm': {
            'morning': 0,
            'evening': 0,
            'night': 0
        },
        'hot': {
            'morning': 1,
            'evening': 2,
            'night': 1
        },
    },
    'hot': {
        'cold': {
            'morning': -4,
            'evening': -5,
            'night': -4
        },
        'warm': {
            'morning': -2,
            'evening': 0,
            'night': -2
        },
        'hot': {
            'morning': 0,
            'evening': 0,
            'night': 0
        },
    }
}

def getInput():
    location = input("Enter Location (Cold, Warm, Hot) : ").lower()
    preference = input("Enter Preference (Cold, Warm, Hot) : ").lower()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if("05:00:00" <= current_time <= "13:00:00"): 
        time = 'morning'
    elif ("13:00:00" <= current_time <= "20:00:00"):
        time = 'evening'
    else:
        time = 'night'
    
    return [location, preference, time]

if __name__ == "__main__":
    [location, preference, time] = getInput()    
    currentTemp = int(input("Enter Temperature : "))
    print("Temperature (Before): " + str(currentTemp))
    currentTemp += rulebase[location][preference][time]
    print("Temperature (Adjusted): " + str(currentTemp))
