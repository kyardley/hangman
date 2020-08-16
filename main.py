#importing the time module
import time
from pics import HANGMANPICS

#welcoming the user



def main():
    print ("Welcome to Hangman.")
    print(HANGMANPICS[0])
    name = input("What is your name? ")

    print ("")

    #wait for 1 second
    time.sleep(1)

    print ("Start guessing...")
    time.sleep(0.5)


if __name__ == "__main__":
    main()
