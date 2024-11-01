'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''

class Solution:
    def my_sqrt(self, x:int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
    
if __name__ == '__main__':
    my_solution = Solution()
    print(my_solution.my_sqrt(9))