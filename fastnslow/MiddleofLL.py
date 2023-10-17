"""Find middle of LL"""

def midLL(self,head):
    if not head:
        return None
    slow, fast = head, head
    while(fast and fast.next):
        slow, fast = slow.next, fast.next.next
    return slow

"""Find start of cycle"""
 def findCycleStart(self, head):
    #TODO Write your code here
    lengthOfCycle = 0
    slow, fast = head, head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        lengthOfCycle = self.countCycle(slow)
        break
    
    pointer1 = head
    pointer2 = head
    for i in range(lengthOfCycle):
      pointer2 = pointer2.next


    while pointer2 != pointer1:
      pointer1 = pointer1.next
      pointer2 = pointer2.next

    return pointer1


  def countCycle(self, slow):
    current =  slow
    counter = 0
    while True:
      current = current.next
      counter += 1
      if (current == slow):
        return counter
