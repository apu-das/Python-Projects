
####################### Description of the project #####################################
 # Build a Number guessing game, in which the user selects a range.
 # Let’s say the User selected a range, i.e., from X to Y, where X and Y belong to Integer.
 # Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

########################################################################################

import random
import math

# Taking input from the user
lower = int(input('Enter lower bound: '))

# Taking input from the user
upper = int(input('Enter upper bound: '))

# Generating numbers between lower and upper bound
x = random.randint(lower, upper)

# Calculating the minimum number of tries
# Minimum number of guessing = log2(Upper bound – lower bound + 1)
y = round(math.log(upper - lower + 1, 2))
print("\n You've only ", y, " chances to guess the number! \n")

# Initializing the number of guesses.
count = 0

# Checking the condition
while count < y:
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number: "))

    # Checking condition
    if guess == x:
        print('Congratulations you did it in ', count, 'times !')
        # Once the condition satisfied, the loop will break
        break
    elif guess < x:
        print('You guessed too small !')
    elif guess > x:
        print('You guessed too high !')

# If guessing exceeds the required guesses, then show this output
if count >= y:
    print('\n The number is ', x)
    print('\t Good Luck Next Time!')
