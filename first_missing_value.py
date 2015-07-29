def firstMissingPositive(nums):
  '''
   in O(n) time and uses constant space.
  '''
  nums.sort() 
  if not len(nums): return 1
  if nums[0] > 1 : return 1
  for i in range(1,len(nums)):
    if nums[i] != nums[i-1] + 1 and nums[i] > 1 and nums[i] != nums[i-1]:
      return max(nums[i-1] + 1,1)
    
  return max(1, nums[len(nums)-1] + 1 )
  

   
print 3, firstMissingPositive([1,2,0])
print 2, firstMissingPositive([3,4,-1,1])
print 1, firstMissingPositive([3,4,-2,-1])
print 2, firstMissingPositive([1,1,4,-2,-1,0])
print 5, firstMissingPositive([1,2,2,1,3,1,0,4,0])
print 1, firstMissingPositive([2])
