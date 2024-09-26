'''
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters'''


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key=len)
        length = len(shortest_string)
        
        longest_substring = ""
        
        for i in range(length):
            for j in range(i + 1, length + 1):
                substring = shortest_string[i:j]
                
                if all(substring in s for s in strs):
                    if len(substring) > len(longest_substring):
                        longest_substring = substring
        return longest_substring
    

