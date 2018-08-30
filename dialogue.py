if __name__ == "__main__":
    pass
else:
    def main():
        print(
            "~~~~~This program will allow you to change your Mac-address.~~~~~\n\
Please choose from the following options:\n\n\
[1] Show the current Mac-address\n\
[2] Change your Mac-address randomly\n\
[3] Enter a custom Mac-address\n\
[4] Reset the original Mac-address\n\
[5] Exit Program\n"
        )
    def connectionType():
        print(
            "Which Connection do you have?\n\n\
[1] Wifi Connection\n\
[2] Ethernet Connection\n\
[3] Go Back\n"
        )
    def inputError():
        print(
            "Choose from the given options.\n"
        )        
        input("Press any key to continue.")
    def randomMac():
        print(
            "Choose from the follwing options:\n\n\
[1] All random\n\
[2] Random but don't change vendor bytes\n\
[3] Set random vendor Mac-address of the same kind\n\
[4] Set random vendor Mac-address of any kind\n\
[5] List known vendors\n\
[6] Go Back\n"
        )
    def findRef():
        print("Your not crazy, you're just special.\n")