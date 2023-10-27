"""Given the head of a LinkedList and two positions ‘p’ and ‘q’, 
reverse the LinkedList from position ‘p’ to ‘q’."""

  def reverse(self, head, p, q):
      # TODO: Write your code here
    prev,curr, next = None, head, None
    counter = 1

    start = None

    while curr and counter < p: 
      start = curr
      curr = curr.next
      counter += 1
    first = curr

    if not start:
      head = None
    while curr and counter <= q:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      counter += 1

    if start:
      start.next = prev
      
    first.next = curr

    return head or prev
      