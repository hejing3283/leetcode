def searchInsert(nums, t):
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
   
    n = len(nums) 
    if not n: return 0
    if n == 1: return 0 if t <=nums[0] else 1
    pL = 0; pR = n - 1

    while pL < pR and pL >= 0 and pR <= n-1:
      if pR - pL == 1:
	if nums[pR ] >= t and t > nums[pL]:
	  return pR
	elif t <= nums[pL]:
	  return 0
	elif t > nums[pR]:
	  return n
      else:
	pM = (pL + pR ) / 2 
	if t < nums[pM] :
	  pR = pM 
	elif t > nums[pM] :
	  pL = pM
	else:
	  return pM
      
# print 2, searchInsert( [1,3,5,6],5) 
# print 5, searchInsert( [1,3,5,6,7],8) 
# print 4, searchInsert( [1,3,5,6],7) 
# print 0, searchInsert( [1,3,5,6],0) 
# print 0, searchInsert( [],0) 
print 0, searchInsert( [1],1) 
print 0, searchInsert( [1],0) 
print 1, searchInsert( [1],2) 
print 0, searchInsert( [1,1,3],1) 
print 0, searchInsert( [1,3,3],3) 


