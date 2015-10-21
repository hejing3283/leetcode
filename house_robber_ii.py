class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) <=2: return max(nums)
        n = len(nums)
        
        dp = [ 0 for _ in range( n-1 ) ]
        
        dp[0] = nums[0];
        dp[1] = max(nums[:2])
        for i in range(2, n-1):
            dp[i] = max( dp[i-1], dp[i-2] + nums[i] ) 
            
        dp2 = [ 0 for _ in range( n-1 ) ]
        dp2[0] = nums[1];
        dp2[1] = max(nums[1:3])
        for i in range(2,n-1):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1] ) 
        return max(dp2[n-2], dp[n-2])
                