# Note: This is a stripped down version of the text-based adventure game, we will have it all together in a
# Python file called final_game.py

def blue_door_room():
    # The variable treasure_chest is an object type called a list
    # A list maybe empty as well.
    # So our treasure_chest list contains 4 items.
    REPLACE = REPLACE
    print("You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the door")

    # Ask player what to do.
    action = raw_input("What do you do? > ")

    # This is a way to see if the text typed by player is in the list
    if REPLACE in REPLACE:
        print("Oooh, treasure!")
    else:
        print("The guard is more interesting, let's go that way!")

def main():
    # We are ignoring the red door room in this task.
    blue_door_room()

if __name__ == '__main__':
    main()