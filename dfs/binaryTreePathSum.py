    """Given a binary tree and a number ‘S’,
 find if the tree has a path from root-to-leaf such
  that the sum of all the node values of that path equals ‘S’.
  """


def hasPath(self, root, sum):
    # TODO: Write your code here
    if not root:
        return False

    if sum == root.val and not root.left and not root.right:
        return True
    
    return self.hasPath(root.left,sum-root.val) or self.hasPath(root.right, sum-root,val)
