class Solution(object):
    def maximalSquare(self, M):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(M) == 0  : return 0
        n = len(M); m = len(M[0])
        
        dp = [ [ 0 for _ in range( m) ] for __ in range(n) ] 
        ans = 0 
        for i in range(n):
            for j in range(m):
                dp[i][j] = int(M[i][j])
                if i and j and int( M[i][j] ):
                    dp[i][j] = min( dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                ans = max(ans, dp[i][j] ) 
        return ans * ans
        