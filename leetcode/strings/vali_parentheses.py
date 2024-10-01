'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Hint:
    Use a stack of characters
    When you encounter an opening bracket, push it to the top of the stack
    When you encounter a closing bracket, check if the top of the stack was the opening for it.
        If yes, pop it from the stack, else return false.
'''
from collections import deque


class Solution:
    def is_valid_parentheses(self, s:str) -> bool:
        characters = ['(', ')', '{', '}', '[', ']']
        stack = deque()
        opening_braces = ['(', '[', '{']
        
        for char in characters:
            if char in opening_braces:
                stack.append(char) 
            else:
                if not stack or (char == '(' and stack.peek != ')') or (char == '[' and stack.peek != ']') or (char == '{' and stack.peek != '}'):
                    return False
                return True
            
if __name__ == '__main__':
    sol = Solution()
    s = '([}'
    print(sol.is_valid_parentheses(s))
