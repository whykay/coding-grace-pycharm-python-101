REPLACE:
    print("You enter a room, and you see a red door to your left and a blue door to your right.")

def main():
    player_name =  raw_input("What's your name? >")
    print("Your name is {}".format(player_name.upper()))

    # Calls another function, declare it above.
    REPLACE

if __name__ == '__main__':
    main()