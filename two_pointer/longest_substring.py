'''
Given an array of characters, find the length of the longest substring withot repeating characters.

Example: abcabcbb
Output: 3
'''

class Solution:

    def length_of_longest_substring(self, s: str) -> int:
        left = 0
        result = 0
        string_set = set()

        for right in range(len(s)):
            while s[right] in string_set:  # there is a duplicate/ repeating charaacter
                string_set.remove(s[left])  # remmove the leftmost character
                # increment the left pointer and add the rightmost character into the sets
                left += 1
            string_set.add(s[right])
            result = max(result, right - left + 1)  # the result is the maximum between the result, and the current length of the array

        return result
    

if __name__ == '__main__':
    s = 'abcabcbb'
    res = Solution()
    print(f'The lenght of the largest substring is {res.length_of_longest_substring(s)}')