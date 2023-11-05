"""Given a binary tree, populate an array to represent its 
zigzag level order traversal. You should populate the values of all nodes
' of the first level from left to right, then right to left for the next 
level and keep alternating in the same manner for the following levels.
"""

  def traverse(self, root):
    result = []
    # TODO: Write your code here
    queue = deque()
    queue.append(root)
    direction = True
    while queue:
        n = len(queue)
        level = deque()
        for i in range(n):
            curr = queue.popleft()
            if direction:
                level.append(curr.val)
            else:
                level.appendleft(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        direction = not direction  
        result.append(list(level))
    return result


    
1
23
4567
