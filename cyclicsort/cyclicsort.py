"""We are given an array containing n objects. Each object, when created, 
was assigned a unique number from the range 1 to n based on their creation sequence.
This means that the object with sequence number 3 was
 created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation 
sequence number in O(n) and without using any extra space. 
For simplicity, let’s assume we are passed an integer array 
containing only the sequence numbers, 
though each number is actually an object.

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
"""

  def sort(self, nums):
    # TODO: Write your code here
    i = 0
    while i < len(nums):
        #J is the index num[i] should be placed at
        j = nums[i] - 1
        #if number not at index should be placed at swap
        if nums[i] != nums[j]:
            nums[i], nums[j]= nums[j], nums[i]
        else:
            i += 1
    return nums

