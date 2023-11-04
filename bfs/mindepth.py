"""Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along
 the shortest path from the root node to the nearest leaf node.

"""

  def findDepth(self, root):
    minimumTreeDepth = 0
    # TODO: Write your code here
    if not root:
        return minimumTreeDepth

    queue = deque()
    queue.append(root)
    while queue:
        n = len(queue)
        minimumTreeDepth += 1
        for _ in range(n):
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)
            else:
                return minimumTreeDepth
            if curr.right:
                queue.append(curr.right)
            else:
                return minimumTreeDepth
    return minimumTreeDepth
