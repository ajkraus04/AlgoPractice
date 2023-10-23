"""We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
 The array can have duplicates, which means some numbers will be missing.
  Find all those missing numbers.
  
 Input: [2, 3, 1, 8, 2, 3, 5, 1]
 Output: 4, 6, 7
  
  """

  def findNumbers(self, nums):
    missingNumbers = []
    # TODO: Write your code here
    i,n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)
    return missingNumbers
