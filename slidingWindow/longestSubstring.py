"""Given a string with lowercase letters only, 
if you are allowed to replace no more than ‘k’ letters with any letter, 
find the length of the longest substring having the same letters after replacement.

EX:
    Input: String="aabccbb", k=2  
    Output: 5  
"""


  def findLength(self, str1, k):
      max_length = float('inf')
      # TODO: Write your code here
      windowStart = 0
      char_occurences = {}
      for windowEnd in range(len(str1)):
        char_occurences[str1[windowEnd]] = char_occurences.get(str1[windowEnd], 0) + 1
        while sum(char_occurences.values()) - max(char_occurences.values()) > k:
            char_occurences[str1[windowStart]] -= 1
            if char_occurences[str1[windowStart]] == 0:
                del char_occurences[str1[windowStart]]
            windowStart += 1
        max_length = max(max_length, windowEnd - windowStart + 1)
      return max_length
