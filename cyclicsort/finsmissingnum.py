"""We are given an array containing n distinct numbers taken from the range 0 to n. 
Since the array has only n numbers out of the total n+1 numbers,
 find the missing number.
 
Input: [0, 1, 4, 3]
Output: 2
 """
def findMissingNumber(self, nums):
    n = len(nums)
    # TODO: Write your code here
    i = 0
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else: 
            i += 1 
    
    for i in range(n):
        if nums[i] != i:
            return i
    return n




 
