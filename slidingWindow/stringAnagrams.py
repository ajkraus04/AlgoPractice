"""Given a string and a pattern, find all anagrams of the pattern in the given string.

Input: String="ppqp", Pattern="pq"  
Output: [1, 2]  
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

"""

class Solution:
  def findStringAnagrams(self, str1, pattern):
    result_indices = []
    # TODO: Write your code here
    windowStart, matches = 0, 0
    char_freq = {}

    for chr in pattern:
      char_freq[chr] = char_freq.get(chr, 0) + 1
    
    for windowEnd in range(len(str1)):
      rightChar = str1[windowEnd]
      if rightChar in char_freq:
        char_freq[rightChar] -= 1
        if char_freq[rightChar] == 0:
          matches += 1
      
      if matches == len(char_freq):
        result_indices.append(windowStart)
      
      if windowEnd >= len(pattern) - 1:
        leftChar = str1[windowStart]
        windowStart += 1
        if leftChar in char_freq:
          if char_freq[leftChar] == 0:
            matches -= 1
          char_freq[leftChar] += 1
    return result_indices
