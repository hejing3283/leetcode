class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def pNodes(self):
      while self:
	print self.val,
	self = self.next

# @param {ListNode} head
# @param {integer} k
# @return {ListNode}
def reverseKGroup(head, k) :
  def reverse(prev, end ):
    ''' given the start node and end node 
     Reverse a link list between pre and next exclusively
     an example:
     a linked list:
     0->1->2->3->4->5->6
     |           |
     pre        next
     after call pre = reverse(pre, next)
     0->3->2->1->4->5->6
	      |  |
	    pre next
	
    return the reversed list's last node, which is the precedence of parameter next
    '''
    curr = prev.next
    temp = curr.next
    while temp != end and temp :
      curr.next = temp.next
      temp.next = prev.next
      prev.next = temp
      temp = curr.next 
    return curr 

  if not head or not head.next or k < 2: return head
  dummy = ListNode(-1); dummy.next = head; prev = dummy
  counter = 0
  while head != None:
    counter += 1
    if  counter % k == 0 :
      prev = reverse(prev, head.next)
      head = prev.next
    else:
      head = head.next

  return dummy.next

a = [1,2,3,4,5] 
l1 = ListNode(a[0])
l1.next = ListNode(a[1])
l1.next.next = ListNode(a[2])
l1.next.next.next = ListNode(a[3])
l1.next.next.next.next= ListNode(a[4])

p = reverseKGroup( l1, 3)
print "out 3 ", l1.pNodes(), p.pNodes()
p = reverseKGroup( l1, 2)
print "out 2 ", p.pNodes()
p = reverseKGroup( l1, 2)
print "k=2: ",l1.pNodes() , p.pNodes()

