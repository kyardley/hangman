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
        f.close()
        return selection

def printword(word):
    temp=''
    for char in word:
        temp += char
        temp += ' '
    print(temp)

def addchar(word, guess, index):
    word[index] = guess
    return word

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
    SELECTWORD=True
    while SELECTWORD==True:
        answer=selectword()
        length=len(answer)
        print("Your word has {} characters".format(length))
        print(answer)
        if input("Do you want to play with this word? (Y/N)") == "Y":
            SELECTWORD=False
    word=list(answer)
    for i in range(0,length):
        word[i]='_'

    print ("Start guessing...")

    time.sleep(0.5)
    guesses = ''
    while(fails <=ALLOWED_FAILS):
        hangmanpic(fails)
        printword(word)
        guess=input("Guess a character: ")
        guesses += guess
        #check guess
        index=answer.find(guess)
        if index != -1:
            print('Yay')
            word=addchar(word, guess, index)
            printword(word)
        else:
            fails += 1
        print(guesses)



if __name__ == "__main__":
    main()
