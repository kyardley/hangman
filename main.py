#import
import time
from pics import HANGMANPICS
from csv import reader
import random

#Function to display the Hangman Picture
def hangmanpic(index):
    print(HANGMANPICS[index])

#Function to select word from wordbank
def selectword():
    with open('Hangman_wordbank', 'r') as f:
        csv_reader = reader(f)
        words = list(csv_reader)
        selection=random.choice(words[0])
        return selection

def main():
    fails=0
    ALLOWED_FAILS=6
    print ("Welcome to Hangman.")
    hangmanpic(fails)
    name = input("What is your name? ")
    print ("")




    #wait for 1 second
    time.sleep(1)
    print("Hi, {}. Let's play!".format(name))
    time.sleep(1)

    word=selectword()
    length=len(word)
    print("Your word has {} characters".format(length))
    print(word)
    print ("Start guessing...")
    time.sleep(0.5)

    while(fails <=ALLOWED_FAILS):
        print(fails)
        hangmanpic(fails)
        fails +=1 


if __name__ == "__main__":
    main()
