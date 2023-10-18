"""Given an array of positive integers and a number ‘S,’ 
find the length of the smallest contiguous subarray 
whose sum is greater than or equal to 'S'. 
Return 0 if no such subarray exists.

Example: [2,1,5,2,3,2], 7
output: 2
"""





def findMinSubArray(s, arr):
    output = float('inf')
    windowSum, windowStart = 0.0, 0 
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowSum >= s:
            print(windowEnd-windowStart)
            output = min(output, windowEnd-windowStart)
            windowSum -= arr[windowStart]
            windowStart += 1
    return output


