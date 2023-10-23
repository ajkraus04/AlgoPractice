"""We are given an unsorted array containing n numbers taken from the range 1 to n.
 The array has some numbers appearing twice, 
 find all these duplicate numbers using constant space.
 
Input: [3, 4, 4, 5, 5]
Output: [4, 5]
 """

  def findNumbers(self, nums):
    duplicateNumbers = []
    # TODO: Write your code here
    i,n = 0, len(nums)
    while i < n:
        if nums[i] != i+1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                duplicateNumbers.append(nums[i])
                i += 1
        else:
            i += 1
    return duplicateNumbers
