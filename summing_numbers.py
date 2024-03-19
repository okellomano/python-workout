'''Work out #2:
    Implements a function that sums a arbitrary number of numbers.
    Like a re-implementation of the sum() in python.
    
    We will use the splat (*) operator.
'''


def my_sum(numbers, start=0):
    total = start
    for number in numbers:
        total += number
    return total


def my_average(numbers):
    return my_sum(numbers) / len(numbers)


def list_of_words(words):
    '''Takes a list of words and returns a tuple conatining the length of the shortest word, longest word, and
        the average length of words. 
     
     '''
    if not words:
        return (0, 0, 0)
    
    shortest_length = float('inf')
    longest_length = 0
    total_length = 0
    
    for word in words:
        word_length = len(word)
        total_length += word_length
        
        if word_length < shortest_length:
            shortest_length = word_length
            
        if word_length > longest_length:
            longest_length = word_length
            
    average_length = total_length / len(words)
    
    
    return (shortest_length, longest_length, average_length)

def sum_objects(elements, start=0):
    '''Takes a list of objects and sums objects that either are integers or can be converted to integers, while ignoring the rest. '''
    total = start
    
    for element in elements:
        try:
            num = int(element)
            total += num
        except (ValueError, TypeError):
            pass

    return total


if __name__ == '__main__':
    print(my_sum([1, 2, 3, 6], 8))
    print(f"For words: {list_of_words(['to', 'take', 'somebody', 'love', 'you', 'trees'])}")
    # print(f'The average is: {my_average(1, 2, 3, 6, 7)}')
    
    print(sum_objects([4, 6, '8', 'string']))