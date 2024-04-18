'''Takes in a string and returns a sorted string. cdba would be sorted to abcd. '''

def string_sort():
    '''Sorts a single string. eg (Tea)'''
    string_to_sort = input('Enter the string: ')
    
    if len(string_to_sort) == 1:
        return string_to_sort
    
    return ''.join(sorted(string_to_sort))

def multi_string_sort():
    '''Sorts multiple strings individually, eg(Tea and bread). '''
    the_string = input('Enter the string to sort: ')
    
    words = the_string.split()
    
    sorted_words = []
    
    for word in words:
        sorted_words.append(''.join(sorted(word)))
          
    return ','.join(sorted_words )


def last_word_alphabetically(file_path):
    '''Returns the last word, alphabetically, in a text file
    
    Steps:
    1. Read the text file line by line.
    2. Split each line into words.
    3. Flatten the list of words.
    4. Find the maximum word alphabetically using the max() function
    '''
    
    with open(file_path, 'r') as file:
        words = [word.strip() for line in file for word in line.split()]
        
        return max(words)
    

def longest_word(file_path):
    '''Returns the longest word in a text file
    
    Steps:
    1. Read the text file line by line.
    2. Split each line into words.
    3. Flatten the list of words.
    4. Find the word with the maximum length using the max() function with a custom key function.
    
    '''
    
    with open(file_path, 'r') as file:
        words = [word.strip() for line in file for word in line.split()]
        
        return max(words, key=len)
    
    
if __name__ == '__main__':
    # print(string_sort())
    print(multi_string_sort())