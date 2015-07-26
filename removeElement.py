def removeElement(nums, val):
  n = len(nums)
  rev = 0 ; i = 0 
  while i < n - rev + 1 and nums:
    # print "-", i, rev, n-rev, nums
    p = nums.pop(0)
    if val == p :
      rev += 1
    else: 
      nums.extend([p])
      i += 1
  return n - rev, nums

print  removeElement( [1,2,3,1,2,4,5], 1 )
print  removeElement( [], 1 )
print  removeElement( [1,1], 1 )
print  removeElement( [1,1,1], 1 )
	    
