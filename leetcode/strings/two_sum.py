'''
Given an array of integers already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Input: numbers[2, 7, 11, 15], target = 9
'''

class Solution:
    def two_sum(arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:

            sum = arr[left] + arr[right]

            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        
        return arr
    

if __name__ == '__main__':
    sol = Solution
    numbers = [2, 7, 11, 15]
    target = 9

    print(sol.two_sum(numbers, target))

