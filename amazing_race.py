# Goal: Generate list of required rides to win "Amazing Race" at KI. Including roadblocks and non fast lane rides.

import random

welcome = "Prepare yourself! You are about to compete in a challenge not for the motion sick!"

instructions = "1. Decide how many rides will be included in the challenge. \n2. Every member must participate in the ride unless height restrictions forbide it. \n3. Your team will take a picture with ALL members in front of the ride sign after completion of each ride. \n4. After your team has completed every ride (including any additional obstacles), meet the others back at the Eiffel Tower for verification."

all_rides = ['Adventure Express', 'Backlot Stunt Coaster', 'Banshee', 'The Bat', 'The Beast', 'Diamondback', 'Flight of Fear', 'Flying Ace Aerial Chase', 'Great Pumpkin Coaster', 'Invertigo', 'Mystic Timbers', 'Orion', 'The Racer', 'Woodstock Express', 'Delirium', 'Drop Tower', 'Windseeker', 'Boo Blasters', 'Congo Falls', 'Dodgem', 'Eiffel Tower', 'Grand Carousel', 'K.I. & Miami Valley Railroad', 'Kings Mills Antique Autos', 'Monster', 'Race for Your Life Charlie Brown', 'Scrambler', 'Shake, Rattle, & Roll', 'Viking Fury', 'White Water Canyon', 'Zephyr']

road_blocks = ["Reride previous ride", "No Fast Lane allowed on next ride!", "Take a water break"]


def generate():
    length = int(input("How many rides do you want included? "))
    for ride in range(length):
        ride = random.choice(all_rides)
        print(ride)
        all_rides.remove(ride)

    if length > 5:
        print(random.choice(road_blocks))

print(welcome)
print(instructions)

participants = int(input("How many people are playing today? "))

print("Please split into two teams of", participants/2)

generate()