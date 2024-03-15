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
    attemps = 1
    
    print('** You have three chances to guess my number **')
    
    while True:
        if attemps <= 3: 
            user_number = int(input(f'I have a number between 1 and 200, guess the number. [Attempt #{attemps}]: '))
            
            if user_number > number:
                print(f'Your guess of {user_number} is too high.')
            elif user_number < number:
                print(f'Your guess of {user_number} is too low')
            elif user_number == number:
                print(f'Just right. The right answer is {user_number}')
                break
        else:
            print(f'\nYou are out of attemps. Try again next time. My number was {number}')
            break
        
        attemps += 1
        
        
if __name__ == '__main__':
    guess_number()
    