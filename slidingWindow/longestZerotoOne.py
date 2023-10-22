"""Given an array containing 0s and 1s, 
if you are allowed to replace no more than ‘k’ 0s with 1s,
find the length of the longest contiguous subarray having all 1s.

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2  
Output: 6  
"""
def findLength(self, arr, k):
    max_length = 0
    #Write code under here
    char_occurences = {}
    windowStart = 0
    for windowEnd in range(len(arr)):
        char_occurences[arr[windowEnd]] = char_occurences.get(arr[windowEnd], 0) + 1
        while 0 in char_occurences and char_occurences[0] > k:
            char_occurences[arr[windowStart]] -= 1
            windowStart += 1
        max_length = max(max_length, windowEnd-windowStart+1)
    return max_length
