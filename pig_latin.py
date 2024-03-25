''' If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the word. So “air” becomes “airway” and “eat” becomes “eatway.”
If the word begins with any other letter, then we take the first letter, put it on the  end  of  the  word,  and  then  add  “ay.”  
Thus,  “python”  becomes  “ythonpay”and “computer” becomes “omputercay.”


Again, we check to see if the word contains two different vowels.
If  it  does,  we  don’t  move  the  first  letter  to  the  end.  Because  the  word  “wine”contains two different vowels (“i” and “e”), we’ll add “way” 
to the end of it, giv-ing us “wineway.” By contrast, the word “wind” contains only one vowel, so wewould move the first letter to the end and add “ay,” 
rendering it “indway.” Howwould you check for two different vowels in the word

'''

import string


def pig_latin():    
    word = input('Enter a word: ').strip()
    vowels = 'aeiouAEIOU'
    
    # We can use sets to find all vowels in a word, and then find the length of the set
    num_vowels = len(set(v for v in word if v in vowels))
        
    if not word:
        print('Error: Please enter a word')
        return
    
    # check if the word ends in a punctuation. The output should also have a punctuation at the end
    if word[-1] in string.punctuation:
        punctuation = word[-1]
        word = word[:-1]
    else:
        punctuation = ''
    
    if word[0] in vowels or num_vowels > 1:
        pig_latin_word =  f'{word}way'.title()
    else:
        pig_latin_word = f'{word[1:]}{word[0]}ay'.title()
        
    return pig_latin_word + punctuation


def count_vowels(word):
    '''Counts the number of vowels in a word. '''
    return sum(1 for v in word if v in 'aeiouAEIOU')
       
        
if __name__ == '__main__':
    print(f'Latin Word: {pig_latin()}')
    