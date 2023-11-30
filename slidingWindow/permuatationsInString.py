"""Given a string and a pattern, find out if the string contains any permutation of the pattern.

Input: String="oidbcaf", Pattern="ABC"   
Output: true   
Explanation: The string contains "bca" which is a permutation of the given pattern.
"""


import math

class Solution:
  def findPermutation(self, str1, pattern):
    # TODO: Write your code here
    windowStart, matched = 0, 0
    char_freq = {}

    for chr in pattern:
      char_freq[chr] = char_freq.get(chr, 0) + 1
    
    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar in char_freq:
           char_freq[rightChar] -= 1
           if char_freq[rightChar] == 0:
              matched += 1
        
        if matched == len(char_freq):
           return True

        if windowEnd >= len(pattern) - 1:
           leftChar = str1[windowStart]
           windowStart += 1
           if leftChar in char_freq:
             if char_freq[leftChar] == 0:
                matched -= 1
             char_freq[leftChar] += 1

    return False


