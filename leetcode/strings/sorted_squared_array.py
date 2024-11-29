'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = 0
        right = l - 1

        new_array = [0]*l

        for k in reversed(range(l)):
            if nums[left] ** 2 > nums[right] ** 2:
                new_array[k] = nums[left] ** 2
                left += 1
            else:
                new_array[k] = nums[right] ** 2
                right -= 1
        return new_array
    