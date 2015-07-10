#!/usr/bin/python
#J.HE
#Desp.:
def twoSum( a, t ):
  ## return indices of the 2 numbers, idx1 < idx2, not 0-based
  ## input array of integers, target number
  len_a = len(a)
  for idx1 in range(0, len_a-1):
    diff  = t - a[ idx1 ]
    for idx2 in range(len_a-1, idx1, -1) :
      if ( a[idx2] ==  diff) :
	result = [ idx1+1, idx2+1 ]
	break
  return result

print( twoSum([2,7,11,15], 9 ) )
print( twoSum([2,7,11,15], 17 ) )
