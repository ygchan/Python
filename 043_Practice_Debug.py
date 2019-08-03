# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# Practice Project - Debugging coin toss
# The program has a few bugs and please fix it by running it through.

import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()

    if toss == guess:
        print('You got it')
    else:
        print('Nope. You are really bad at this game.')
