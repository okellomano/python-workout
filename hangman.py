'''Python program to illustrate the Hangman Game. '''

import random
from collections import Counter

words = '''
    apple banana mango strawberry orange grape pineapple lemon
    apricot coconut watermelon cherry papaya berry peach lychee
    muskmelon
'''

words = words.split(' ')
word = random.choice(words)


def hangman_game():
    print('Guess the word! HINT: The word is a fruit...')
    
    # Give empty spaces equivalent to the length of the word
    for i in word:
        print('_', end=' ')
    print()
    
    playing = True
    
    guesses = ''
    
    chances = len(word) + 3
    correct = 0
    flag = 0
    
    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1
            
            try:
                guess = input('Enter a letter to guess: ')
            except:
                print('Only letters are allowed!')
                continue
            
            if not guess.isalpha():
                print('Only letters are allowed!')
                continue
            elif len(guess) > 1:
                print('Only single letter guesses are allowed!')
                continue
            elif guess in guesses:
                print('You have already guessed that letter!')
                continue
            
            # If the letter is guessed correctly, count the number of times the guessed letter occurs in the word
            if guess in word:
                k = word.count(guess)
                
                # add the guessed letter as many times at it occurs
                for _ in range(k):
                    guesses += guess
                    
            # print the word
            for char in word:
                if char in guesses and Counter(guesses) != Counter(word):
                    print(char, end=' ')
                    correct += 1
                elif Counter(guesses) == Counter(word):
                    print(f'The word is: {word}')
                    flag = 1
                    print('Congratulations!')
                    break
                    break
                else:
                    print('_', end=' ')
        
        if chances <= 0 and Counter(guesses) != Counter(word):
            print(f'\nYou lost! Try again...\nThe word was {word}')
    except KeyboardInterrupt:
        print('\nBye!')        
        exit()
        
        
if __name__ == '__main__':
    hangman_game()           
                
