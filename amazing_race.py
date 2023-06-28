# Goal: Generate list of required rides to win "Amazing Race" at KI. Including roadblocks and non fast lane rides.

import random

participants = int(input("How many people are playing today? "))

print("Please split into two teams of", participants/2)

all_rides = ['Adventure Express', 'Backlot Stunt Coaster', 'Banshee', 'The Bat', 'The Beast', 'Diamondback', 'Flight of Fear', 'Flying Ace Aerial Chase', 'Great Pumpkin Coaster', 'Invertigo', 'Mystic Timbers', 'Orion', 'The Racer', 'Woodstock Express']

road_blocks = ["Reride previous ride", "No Fast Lane allowed on next ride!", "Take a water break"]


def generate():
    length = int(input("How many rides do you want included? "))
    for ride in range(length):
        ride = random.choice(all_rides)
        print(ride)
        all_rides.remove(ride)

    if length > 5:
        print(random.choice(road_blocks))

generate()