"""Given a binary tree, populate an array to
 represent its level-by-level traversal.
 You should populate the values of all nodes of each 
 level from left to right in separate sub-arrays.
 """
from collections import deque

def traverse(self, root):
    result = []
    # TODO: Write your code here
    queue = deque()
    queue.append(root)
    while queue:
        n  = len(queue)
        level = []
        for _ in range (n):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            level.append(curr.val)
        result.append(level)
    return result
