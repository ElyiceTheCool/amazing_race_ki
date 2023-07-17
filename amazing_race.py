# Goal: Generate list of required rides to win "Amazing Race" at KI. Including roadblocks and non fast lane rides.

import random

welcome = "Prepare yourself! You are about to compete in a challenge not for the motion sick!"

instructions = "INSTRUCTIONS: \n1. Decide how many rides will be included in the challenge. \n2. Every member must participate in the ride unless height restrictions forbide it. \n3. Your team will take a picture with ALL members in front of the ride sign after completion of each ride. \n4. After your team has completed every ride (including any additional obstacles), meet the others back at the Eiffel Tower for verification and celebration."

all_rides = ['Adventure Express', 'Backlot Stunt Coaster', 'Banshee', 'The Bat', 'The Beast', 'Diamondback', 'Flight of Fear', 'Flying Ace Aerial Chase', 'Invertigo', 'Mystic Timbers', 'Orion', 'The Racer', 'Woodstock Express', 'Delirium', 'Drop Tower', 'Windseeker', 'Boo Blasters', 'Cargo Loco', 'Congo Falls', 'Dodgem', 'Eiffel Tower', 'Grand Carousel', 'K.I. & Miami Valley Railroad', 'Kings Mills Antique Autos', 'Monster', 'Race for Your Life Charlie Brown', 'Scrambler', 'Shake, Rattle, & Roll', 'Sol Spin', 'Viking Fury', 'White Water Canyon', 'Zephyr']

road_blocks = ["Reride previous ride", "No Fast Lane allowed on next ride!", "Take a water break!", "Ride in the front row of the next ride", "Ride in the back row of the next ride"]

# into to program
print(welcome)
print(instructions)

# user input categories
participants = int(input("How many people are playing today? "))
print("Please split into two teams of", participants/2)
length = int(input("How many rides do you want included? "))
ride_list = []

# generates a list of rides that must be completed
def generate():
    for ride in range(length):
        ride = random.choice(all_rides)
        ride_list.append(ride)
        all_rides.remove(ride)

    print(ride_list)

# checks for ride specific roadblock requirements
def checks():
    if length < 5:
        pass
    elif length >= 5 and length < 10 and "Cargo Loco" in ride_list:
        print("Must ride lime barrel on Cargo Loco")
    elif length >= 5 and length < 10 and "Mystic Timbers" in ride_list:
        print("Must ride blue train on Mystic!")
    elif length >= 10:
        for x in range(2):
            roadie = random.choice(road_blocks)
            print(roadie)
    else:
        print(random.choice(road_blocks))


generate()
checks()

# TODO: Insert roadblock randomly into ride list each time
# TODO: Assign each team a different starting ride