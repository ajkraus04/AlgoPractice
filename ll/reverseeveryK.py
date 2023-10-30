"""Given the head of a LinkedList and a number ‘k’, 
reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list 
with less than ‘k’ elements, reverse it too."""

  def reverse(self, head, k):
    # TODO: Write your code here
    current, previous = head, None
    while True:
        last_of_previous_part = previous
        last_of_sub_list = current

        i=0
        next = None
        while i < k and current:
          next = current.next
          current.next = previous
          previous = current
          current = next
          i += 1
        
        if not last_of_previous_part:
            head = previous
        else:
            last_of_previous_part.next = previous

        last_of_sub_list.next = current
        
        if not current:
            break
        
        previous = last_of_sub_list
    return head


   