def get_player_name():
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    TODO = raw_input("What's your name? > ")

    # This is just an alternative name that the game wants to call the player
    alt_name = "Rainbow Unicorn"
    answer = raw_input("Your name is {}, is that correct? [Y|N] > ".format(alt_name.upper()))
    if answer.TODO() in ["y", "yes"]:
        TODO
        print("You are fun, {}! Let's begin our adventure!").format(name.upper())
    elif answer.lower() in ["n", "no"]:
        print("Ok, picky. {} it is. Let's get started on our adventure.".format(name.upper()))
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(alt_name.upper()))
        TODO

    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in
    # get_player_name() function.
    # This is why indentation is important, variables declared in this block only exists in that block
    return TODO

TODO =  TODO
print(TODO)