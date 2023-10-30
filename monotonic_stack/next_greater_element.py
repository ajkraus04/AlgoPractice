"""Given two integer arrays nums1 and nums2, return an array answer such that answer[i]
 is the next greater number for every nums1[i] in nums2. The next greater element 
 for an element x is the first element to the right of x that is greater than x. 
 If there is no greater number, output -1 for that number.

The numbers in nums1 are all present in nums2 and nums2 is a permutation of nums1.


Input: nums1 = [4,2,6], nums2 = [6,2,4,5,3,7]
Output: [5,4,7]
Explanation: The next greater number for 4 is 5, for 2 is 4, and for 6 is 7 in nums2.
"""

def next_greater_element(self, nums1, nums2):
        # Initialize stack and hashmap
        stack, hashmap = [], {}
        #loop through all nums in nums2 array
        for num in nums2:
            #if theres stuff in stack and num is next greater element to last num in stack
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            # append the num to the stack
            stack.append(num)
        # return all the next greater element values
        return [hashmap.get(num, -1) for num in nums2]
