treasure_chest = ["diamonds", "gold", "silver", "sword"]

for treasure in treasure_chest:
    print(treasure)

print("What do you want to do?")

print("Take all {} treasure, press '1'".format(TODO))
print("Leave it, press '2'")

treasure_choice = raw_input("> ")

if treasure_choice == "1":
    print("TODOWoohoo! Bounty and a shiney new sword. /drops your crappy sword in the empty treasure chest.")
    print("TODOYou just received [{}]".format(TODO))
elif treasure_choice == "2":
    print("It will still be here (I hope), right after I get past this guard")
