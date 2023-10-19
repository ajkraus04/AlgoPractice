"""Given an array of positive integers and a number ‘S,’ 
find the length of the smallest contiguous subarray 
whose sum is greater than or equal to 'S'. 
Return 0 if no such subarray exists.

Example: [2,1,5,2,3,2], 7
output: 2
"""





def findMinSubArray(s, arr):
    output = float('inf')
    windowSum 0.0
    windowEnd, windowStart = 0, 0
    while windowEnd < len(arr):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            output = min(output, windowEnd-windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1
        windowEnd += 1
    return output

# loop through arr
# as you loop,add val at windowENd To windowSum
# once you hit sum, 
#check if val at windowStart can be removed from windowSum yet have windowSum still >= S
#if yes, remove val at windowStart, decrease output, increase windowStart by + 1
#repeat this check on val at windowStart until we can no longer cutoff indexes , making that subarray no longer satisfy condition, 
#continue looking for subarrays that satisfy what we;re looking for

