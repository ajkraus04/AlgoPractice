"""Given a string, find the length of the longest 
substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example: "araaci", 2
output = 4
"""
def findLength(self, str1, k):
    max_length = 0
    # TODO: Write your code here
    char_occurences = {}
    windowStart = 0
    for windowEnd, char in enumerate(len(str1)):
        char_occurences[char] = char_occurences.get(char, 0) + 1
        while(len(char_occurences)>2):
            char_occurences[str1[windowStart]] -= 1
            if char_occurences[str1[windowStart]] == 0: 
                del char_occurences[str1[windowStart]]
            windowStart += 1
        max_length = max(max_length,windowEnd-windowStart+1)
    return max_length
