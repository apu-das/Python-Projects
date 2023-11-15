# In this game, there is a list of words present, out of which our interpreter will choose 1 random word. 
# The user first has to input their names and then, will be asked to guess any alphabet.
# If the random word contains that alphabet, it will be shown as the output
# (with correct placement) else the program will ask you to guess another alphabet. 
# The user will be given 12 turns(which can be changed accordingly) to guess the complete word.


import random

name= input("What's your name? ")
print("Good Luck!", name)
words= ["Mathematics", "Programming", "Python", "Computer", "Linear", "Science", "Words", "Random"]
word= random.choice(words) #choosing a random word from the list
print("Guess the Charaters")

guesses= ' '
turns= 15        #Any number of turns 

while turns > 0:
    failed= 0    #count the number of times that a user fails

    #one character is taken a time for the input word
    for char in word:
        if char in guesses:  #comparing that character with the character in guesses.
            print(char, end='')
        else:
            print("_")

            failed +=1  #for every failure 1 will be incremented in failure
    
    if failed==0:
        print("\nYou Win, Congratulations!") #User will win the game
        print("\nThe word is: ", word)
        break


    #if user give wrong input then it will ask user to enter another
    print()
    guess= input("Guess a character: ")

    guesses += guess   #every input character will be stored in guesses

    #Check input will the character in word

    if guess not in word:
        turns -=1

        #if charcter doesn't match the word 
        print("Wrong Guess!")
        #print the number of turns left for the user
        print("You have ", + turns, "more guesses.")

        if turns ==0:
            print("You Loose! Better Luck Next Time")
            