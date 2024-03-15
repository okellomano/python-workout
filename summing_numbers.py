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


if __name__ == '__main__':
    print(my_sum([1, 2, 3, 6], 8))
    print(f"For words: {list_of_words(['to', 'take', 'somebody', 'love', 'you', 'trees'])}")
    # print(f'The average is: {my_average(1, 2, 3, 6, 7)}')