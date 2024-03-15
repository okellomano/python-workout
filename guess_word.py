'''Hava a list or words. Choose a random word from the list and let the user guess the chosen word. '''

import random


words = ["cat", "dog", "bird", "fish", "tree", "book", "ball", "frog", "moon", "star"]


def guess_word():
    attemps = 1
    word = random.choice(words)
    
    print('** You wil have three attemps ***')
    
    while True:
        if attemps < 4:
            my_word = input(f'I have chosen a random word from these words:\n {words} \n\n Can you guess which one is it? [Attempt # {attemps}]').casefold()
            
            try:
                my_word_index = words.index(my_word)
            except ValueError:
                print('\nInvalid input. Please enter a word from the list')
                continue
            
            word_index = words.index(word)
            
            if my_word_index == word_index:
                print(f'Got it! My word was: {word}')
                break
            elif my_word_index < word_index:
                print('Choose the word later than that')
            elif my_word_index > word_index:
                print('Choose a word earlier than that')
            
            attemps += 1
            
        else:
            print(f'\nYou are out of attempts. The random word was: {word}')
            break
            
if __name__ == '__main__':
    guess_word()
            
            
