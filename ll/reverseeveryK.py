"""Given the head of a LinkedList and a number ‘k’, 
reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list 
with less than ‘k’ elements, reverse it too."""

  def reverse(self, head, k):
    # TODO: Write your code here
    current, previous = head, None
    while True:
        last_node_previous_part = previous
        last_node_of_sub_list = current
        next = None
        i = 0

        while current and i<k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i+=1

        if last_node_previous_part:
            last_node_previous_part.next = previous 
        else:
            head = previous

        last_node_of_sub_list.next = current

        if not current:
            break
        
        previous = last_node_of_sub_list
    
    return head


   