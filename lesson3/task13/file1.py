guard_moved = TODO

while True:
    next_action = raw_input("[run | door] > ").lower()
    if (next_action == "run") and (guard_moved == True):
        print("Guard was faster than he looks and your world goes dark...")
        TODO
    elif (next_action == "run") and (guard_moved == False):
        print("Guard jumps up and looks the other way, missing you entirely.")
        guard_moved = TODO
    elif (next_action == "door") and (guard_moved == True):
        print("You just slipped through the door before the guard realised it.")
        print("You are now outside, home free! Huzzah!")
        TODO
    elif (next_action == "door") and (guard_moved == False):
        print("Guard was faster than he looks and your world goes dark...")
        TODO
    else:
        print("Not sure what you meant there... try again.")
