class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def pNodes(self):
      while self:
	print self.val,
	self = self.next
      print 

# @param {ListNode} head
# @param {integer} k
# @return {ListNode}
def reverseKGroup(head, k) :
  def reverse(head):
    ''' given the start node and end node '''
    dummy = ListNode(0); 
    while head :
      curr = head.next
      head.next = dummy.next
      dummy.next = head
      head = curr 
    return dummy.next 

  if not head or not head.next or k < 2: return None
  dummy = ListNode(-1); dummy.next = head; prev = dummy
  counter = 0
  while head:
    counter += 1
    if  counter % k == 0 :
      prev = reverse(prev, head.next)
    else:
      head = head.next

  return dummy.next

a = [1,2,3,4,5 ] 
l1 = ListNode(a[0])
l1.next = ListNode(a[1])
l1.next.next = ListNode(a[2])
l1.next.next.next = ListNode(a[3])
l1.next.next.next.next= ListNode(a[4])

print "in", l1.pNodes()
p = reverseKGroup( l1, 3)
print "out 2 ", p.pNodes()
print "in",l1.pNodes()
p = reverseKGroup( l1, 2)
print "out 3 ", p.pNodes()
print "in", l1.pNodes()
p = reverseKGroup( l1, 5)
print "out 5 " , p.pNodes()

