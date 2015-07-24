def mergeTwoLists(l1, l2):
  if (len(l1) > 0) + (len(l2) > 0) != 2 : 
    return l1 + l2  
  elif  l1[-1] <= l2[0]:
    return l1 + l2
  elif l1[0] >= l2[-1]:
    return l2 + l1
  else :
    p1 = 0 ; p2 = 0 
    l12 = [] 
    while p1 < len(l1) and p2 < len(l2):
      if l1[ p1 ]  > l2[ p2 ]:
	l12.append(l2[p2])
	p2 += 1
      elif l1[p1] < l2[p2]:
	l12.append(l1[p1])
	p1 += 1
      else:
	l12.extend( [ l1[p1], l2[p2]] )
	p1 += 1
	p2 += 1
    return l12

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1 = ListNode(1,4); l1 = ListNode(l1,7) l1 = ListNode(l1, None)]; 
l2 = ListNode(-1,0); l2 = ListNode(l2,1) l2 = ListNode(l2, None)]; 

print mergeTwoLists( l1, l2)

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
