"""Given a binary tree and a number ‘S’, 
find all paths from root-to-leaf such that the
 sum of all the node values of each path equals ‘S’.
 """

#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPaths(self, root, required_sum):
    allPaths = []
    # TODO: Write your code here
    self.findAllPathsSum(root, [], required_sum, allPaths)
    return allPaths

  def findAllPathsSum(self, root, keep, required_sum, allPaths):
    if not root:
        return 

    keep.append(root.val)

    if required_sum == root.val and not root.left and not root.right:
        allPaths.append(list(keep))
    else:
        self.findAllPathsSum(root.left,keep,required_sum-root.val,allPaths)
        self.findAllPathsSum(root.right,keep,required_sum-root.val,allPaths)

    del keep[-1]
