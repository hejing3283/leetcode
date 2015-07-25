class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
  def mSort(lists, left, right):
    '''
    sort according to the first value
    '''
    # pL = left; pR = right
    # while pL < right and pR > left:
    #   if lists[left].val > lists[right].val:
	# lists[left], lists[right] = lists[right], lists[left]
    #   else :
	# pL += 1
	# pR -= 1
    # return lists

  # lists =  mSort( lists , 0, 2)
  # # for p in out :
    # print p.val,

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

  c = mergeTwoLists(lists.pop(0) , lists.pop(0) )
  pL = 0; pR = len(lists) - 1
  for  a in lists:
    c = mergeTwoLists(c, a)
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

out = mergeKLists( [l2, l1, l3] )
p = out.next
while p:
  print p.val,
  p = p.next

 
