class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
  if not lists:
    return None
  def mergeTwoLists( a, b ):
    if not a and b:
      return b
    elif not b and a:
      return a 
    elif not a and not b:
      return None
    else:
      if a.val > b.val:
          a, b = b, a
      a.next = mergeTwoLists(a.next, b)
      return a or b

  c = lists.pop(0)  
  while lists:
    c = mergeTwoLists(c, lists.pop(0))
  return c

l1 = ListNode(-1)
l1.next = ListNode(1)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(7)

temp = ListNode(9)
l2 = ListNode(8); l2.next = temp
temp =ListNode(0); temp.next = l2
l2 = temp

temp = ListNode(15)
l3 = ListNode(11); l3.next = temp
temp =ListNode(-3); temp.next = l3
l3 = temp

# out = mergeKLists( [l2, l1, l3] )
out = mergeKLists( [l2] )
out = mergeKLists( [] )
out = mergeKLists( [] )
p = out 
while p:
  print p.val,
  p = p.next

 
