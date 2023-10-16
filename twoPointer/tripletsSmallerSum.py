"""Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, 
and k are three different indices. 
Write a function to return the count of such triplets.

EX: 
Input: [-1,0,2,3], 3
output: 2
"""

def lessTriplets (arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        num1 = arr[i]
        left, right = i+1, n-1

        while left < right:
            threeSum = num1 + arr[left] + arr[right]
            if threeSum < target:
                count += 1
                left += 1
            else: 
                right -= 1
    return count


    print(lessTriplets([-1,2,0,3],3))
                
    