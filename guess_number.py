'''Generates a random number and asks the user to guess the generated number.

Approach #1
    1. Generate the random number using the random module.
    2. Using the input function, ask the user to make a guess.
    3. Convert the input to integer for comparision with the generated number.
    4. If the guess is correct, exit the program. If it's low, print low, and if high print high.
'''

import random


def guess_number():
    number = random.randint(1, 200)
    
    while True:
        user_number = int(input('I have a number between 1 and 200, guess the number: '))
        
        if user_number > number:
            print(f'Your guess of {user_number} is too high.')
        elif user_number < number:
            print(f'Your guess of {user_number} is too low')
        elif user_number == number:
            print(f'Just right. The right answer is {user_number}')
            break
        
        
if __name__ == '__main__':
    guess_number()
    