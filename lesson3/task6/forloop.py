# Note: This is a stripped down version of the text-based adventure game, we will have it all together in a
# Python file called final_game.py

def blue_door_room():
    # The variable treasure_chest is an object type called a list
    # A list maybe empty as well.
    # So our treasure_chest list contains 4 items.
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the door")

    # Ask player what to do.
    action = raw_input("What do you do? > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!")

        #### NEW CODE STARTS HERE
        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = raw_input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # FOR LOOP
            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            REPLACE
                print(REPLACE)
    else:
        print("The guard is more interesting, let's go that way!")

def main():
    # We are ignoring the red door room in this task.
    blue_door_room()

if __name__ == '__main__':
    main()
