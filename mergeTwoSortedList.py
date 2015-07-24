class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
      # @param {ListNode} l1
      # @param {ListNode} l2
      # @return {ListNode}
      def mergeTwoLists(self, l1, l2):
	if l1 and l2:

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
l1 = ListNode(1,4); 
l1.next = 7;  
l1.next = None; 
# l2 = ListNode(-1,0); l2 = ListNode(l2,1) ;l2 = ListNode(l2, None); 

print l1
# print mergeTwoLists( l1, l2)

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
