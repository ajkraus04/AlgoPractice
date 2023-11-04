"""Given a binary tree, populate an array 
to represent the averages of all of its levels.

"""
  def findLevelAverages(self, root):
    result = []
    # TODO: Write your code here
    queue = deque()
    queue.append(root)
    while queue:
        n = len(queue)
        sumlvl = 0
        for i in range(n):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            sumlvl += curr.val
        result.append(sumlvl / n)
    return result
