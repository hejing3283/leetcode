class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def swapPairs(head):
  # @param {ListNode} head
  # @return {ListNode}
  '''
  no or one node

  '''
  if not head or not head.next :
    return head 
  
  dummy = ListNode(-1)
   
  counter = 0
  while head:
    counter += 1
    counter
    first = head 
    dummy.next = second 
    second = head.next
    head = second.next 

    frist.next = dummy
    second.next = first 


    


