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
  def reverse(start,end):
    ''' given the start node and end node '''
    newhead=ListNode(0); newhead.next=start
    while newhead.next != end and start.next :
      tmp  =  start.next
      # print "--", start.val, ":", tmp.pNodes()
      start.next = tmp.next
      tmp.next = newhead.next
      newhead.next = tmp
    return [end, start]

  if not head: return None

  nhead = ListNode(0); nhead.next = head; start = nhead

  while start.next:
    end = start
    for _ in range(k-1):
      end = end.next
      if end == None: 
	return nhead.next
      else:
	continue
    
    res = reverse( start.next, end.next)
    start.next = res[0]
    start = res[1]
  return nhead.next

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

