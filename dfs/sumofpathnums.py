"""Given a binary tree where each node can only have a digit (0-9) value,
 each root-to-leaf path will represent a number. 
 Find the total sum of all the numbers represented by all paths."""

def findSumOfPathNumbers(self, root):
    # TODO: Write your code here
    totalSum = [0]
    self.findValues(root, 0, totalSum)
    return totalSum[0]

def findValues(self, currNode, sum, totalSum):
    if not currNode:
        return
    sum += currNode.val

    if not currNode.left and not currNode.right:
        totalSum[0] += sum

    self.findValues(currNode.left, sum * 10, totalSum) 
    
    self.findValues(currNode.right, sum * 10, totalSum) 

