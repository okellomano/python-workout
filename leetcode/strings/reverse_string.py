'''
Use a stack to reverse a string
'''
from collections import deque


def reversed(s) -> str:
    my_stack = deque()
    reversed_string = deque()
    
    for char in s:
        my_stack.append(char)
    reversed_string = ''
    
    while my_stack:
        reversed_string += my_stack.pop()
        
    return reversed_string


if __name__ == '__main__':
    st = 'God is great!'
    print(reversed(st))
        
        