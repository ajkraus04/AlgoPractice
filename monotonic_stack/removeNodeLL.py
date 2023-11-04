"""Given the head node of a singly linked list, modify the list such that any node that 
has a node with a greater value to its right gets removed. 
The function should return the head of the modified list.

Examples:

Input: 5 -> 3 -> 7 -> 4 -> 2 -> 1
Output: 7 -> 4 -> 2 -> 1
Explanation: 5 and 3 are removed as they 
have nodes with larger values to their right.

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5
Explanation: 1, 2, 3, and 4 are removed as they
 have nodes with larger values to their right.

Input: 5 -> 4 -> 3 -> 2 -> 1
Output: 5 -> 4 -> 3 -> 2 -> 1
Explanation: None of the nodes are removed as none of them 
have nodes with larger values to their right."""


def removeNodes(self, head):
    # TODO: Write your code here
    if not head:
        return None
    stack = []
    curr = head
    while curr:
        while stack and stack[-1].val < curr.val:
            stack.pop()
        if stack:
            stack[-1].next = curr    
        stack.append(curr)
        curr = curr.next
    return stack[0]
