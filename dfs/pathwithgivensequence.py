"""Given a binary tree and a number sequence, 
find if the sequence is present as a 
root-to-leaf path in the given tree."""

class Solution:
  def findPath(self, root, sequence):
    # TODO: Write your code here
    if not sequence or not root:
        return False
    size = len(sequence)
    return self.findPathRecursion(root,0,sequence,size)

  def findPathRecursion(self,curr,idx,sequence, size):
    if not curr or idx >= size:
        return False
    if curr.val != sequence[idx]:
        return False
    
    if idx+1 == size and not curr.left and not curr.right:
        return True
    
    return self.findPathRecursion(curr.left,idx + 1,sequence,size) or self.findPathRecursion(curr.right,idx + 1,sequence,size)
