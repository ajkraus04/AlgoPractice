"""Given a binary tree, connect each node with its level order successor.
 The last node of each level should point to a null node."""    

     def connect(self, root):
        # TODO: Write your code here
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            previous = None
            for _ in range(n):
                curr = queue.popleft()
                if previous:
                    previous.next = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                previous = curr
        return root
