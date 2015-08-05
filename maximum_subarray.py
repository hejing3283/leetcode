class Solution:
  # @param {integer[]} nums
  # @return {integer}
  def maxSubArray1(self, nums):
    ans = None; 
    for i in range( len(nums) ):
      curr = nums[i] 
      for j in range(i + 1, len(nums)): 
	curr += nums[j] 
	if curr > ans :
	  ans = curr
    return ans

  def maxSubArray(self, nums):
    curr = 0 ;
    ans = -100000
    for i in range(len(nums)):
      if curr < 0 :
	curr = 0
      curr = curr + nums[i]
      ans = max(curr, ans)
    return ans


sol = Solution()
print sol.maxSubArray([-2, 1, -3, 4,-1, 2, 1, -5, 4]) 

