class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(w1) + 1
        n = len(w2) + 1
        dp = [ [0 for j in range(n)] for i in range(m)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min( dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] +( 0 if w1[i-1] == w2[j-1] else 1) ) 
        
        return dp[m-1][n-1]