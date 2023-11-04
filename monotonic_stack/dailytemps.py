"""Given an array of integers temperatures representing daily temperatures, 
your task is to calculate how many days you have to wait 
until a warmer temperature. If there is no future day for which 
this is possible, put 0 instead.


Input: temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation: The first day's temperature is 70 and the next day's temperature is 73 which is warmer. 
So for the first day, you only have to wait for 1 day to get a warmer temperature. 
Hence, the first element in the result array is 1. 
The same process is followed for the rest of the days.
"""
def dailyTemperatures(self, temperatures):
    # TODO: Write your code here
    stack = [] #
    res = [0] * len(temperatures)
    
    for i in range(len(temperatures)):
        
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
            
        stack.append(i)
    return res


 def dailyTemperatures(self, temperatures):
    # TODO: Write your code here
    stack = [] #
    hashmap = {}
    res = []
    
    for i in range(len(temperatures)):
        
        while stack and temperatures[i] > stack[-1]:
            res.append(i - hashmap[stack[-1]])
            stack.pop()
            
            
        stack.append(temperatures[i])
        hashmap[temperatures[i]] = i; 
    res.append(0 for nums in stack)
    return
