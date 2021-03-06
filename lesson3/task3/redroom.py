##### ROOMS #####
def blue_door_room():
    # Nothing happens here, let's do one room at the time. :-)
    print("The door knob jiggles but nothing happens.")
    return

def red_door_room():
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    REPLACE = raw_input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    REPLACE
        start_adventure()
    else:
        print("It eats you. Well, that was tasty!")
### END ROOMS ###

def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = raw_input("Do you pick the red door or blue door? > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        # This calls a function that contains stuff that happens in red_door_room
        red_door_room()
    elif door_picked == "blue":
        # This calls a function that contains stuff that happens in blue_door_room
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

def main():
    player_name =  raw_input("What's your name? >")
    print("Your name is {}".format(player_name.upper()))

    start_adventure()

if __name__ == '__main__':
    main()