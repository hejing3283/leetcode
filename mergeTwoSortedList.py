class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
      
a = [-1, 1, 4, 7 ] 
l1 = ListNode(-1)
l1.next = ListNode(1)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(7)

temp = ListNode(9)
l2 = ListNode(8); l2.next = temp
temp =ListNode(0); temp.next = l2
l2 = temp

# print l1.val, l1.next.val, l1.next.next.val, l1.next.next.next.val
# print l2.val, l2.next.val, l2.next.next.val 

out = mergeTwoLists( l1, l2)
p = out
while p :
  print p.val,
  p = p.next

# print out.val, out.next.val, out.next.next.val

# l1 = [1,4,7]; l2 = [1, 8, 9]
# print mergeTwoLists( l1, l2)

# l1 = [1,4,7]; l2 = [8, 9]
# print mergeTwoLists( l1, l2)

# l1 = []; l2 = []
# print mergeTwoLists( l1, l2)

# l1 = [1]; l2 = []
# print mergeTwoLists( l1, l2)
# l1 = [1]; l2 = [-1]
# print mergeTwoLists( l1, l2)
