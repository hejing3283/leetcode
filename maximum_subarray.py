class Solution:
  # @param {integer[]} nums
  # @return {integer}
  def maxSubArray(self, nums):
    start = 0; end = 0
    ans = None; 
    for i in range( len(nums) ):
      curr = nums[i] 
      for j in range(i + 1, len(nums)): 
	curr += nums[j] 
	if curr > ans :
	  ans = curr
    return ans

sol = Solution()
print sol.maxSubArray([-2, 1, -3, 4,-1, 2, 1, -5, 4]) 

