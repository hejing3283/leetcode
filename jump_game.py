class Solution(object):
  def canJump(self, nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      if not nums: return False
      step = nums[0]
      for i in range(1, len(nums)) :
	if step > 0 :
	  step -= 1
	  step = max( step, nums[i] ) 
	else : 
	  return False
      return True


      

nums = [2,3,1,1,4]
s = Solution()
print s.canJump(nums) 

nums = [3,2,1,0,4]
print s.canJump(nums) 

nums = []
print s.canJump(nums) 

nums = [0]
print s.canJump(nums) 

nums = [1,0,5]
print s.canJump(nums) 
					        
