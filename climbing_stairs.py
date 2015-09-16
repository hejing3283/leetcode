class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n 
        dp = [ [ 0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[0][i] = 1; dp[i][0] = 1
            dp[1][i] = 2; dp[i][1] = 2
            
        for i in range(2, n) :
            for j in range(2, n) :
                dp[i][j] = dp[i-1][j-1] + dp[i-2][j-2]
                
        return dp[n-1][n-1]
        