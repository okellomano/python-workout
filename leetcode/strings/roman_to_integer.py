'''Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

class Solution:
    '''To solve this, set the total to 0, and loop through s adding every value, but if the next value is greater than the current value, 
    we need to substract twice the previous value from the current value. Why, e.g IV => I and V which is 6, but the real value is 4, so we 
    subtract 2 * I = 2: 6 - 2 = 4'''
    
    def roman_to_int(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        previous_value = 0
        
        for char in s:
            current_value = romans[char]
            
            if current_value > previous_value:
                total += current_value - 2 * previous_value
            else:
                total += current_value
            previous_value = current_value
        
        return total
    
if __name__ == '__main__':
    test = "MCMXCIV"
    solution1 = Solution()
    print(f'The solution: {solution1.roman_to_int(test)}')
    