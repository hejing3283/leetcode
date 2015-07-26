class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def pNodes(self):
      while self:
	print self.val,
	self = self.next

# 
def swapPairs(head):
  # @param {ListNode} head
  # @return {ListNode}
  '''
  no or one node
  '''
  if not head or not head.next :
    return head 
  
  ## curr is the holder 
  dummy = curr = ListNode(-1)
  dummy.next = head

  while head and head.next:
    p = head.next.next ## get the start of next pair
    curr.next = head.next
    curr.next.next = head
    head.next = p
    curr = head
    head = p

  return dummy.next

a = [1,2,3,4,5] 
l1 = ListNode(a[0])
l1.next = ListNode(a[1])
l1.next.next = ListNode(a[2])
l1.next.next.next = ListNode(a[3])
l1.next.next.next.next= ListNode(a[4])

l1.pNodes()
print 
p = swapPairs(l1)
p.pNodes()
