"""Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
"""


  def reverse(self, head):
    result = None
    # TODO: Write your code here
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    result = prev
    return result
