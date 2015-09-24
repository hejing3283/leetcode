class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 = len(s1); 
        n2 = len(s2)
        n3  = len(s3)
        if s1 == s3 and s1==s2 and s2== '': return True 
        if n3 != n1+n2: return False
        if list(s3).sort() != list(s1 + s2).sort() : return False 
        
        dp = [ [False for i in range(n2 + 1) ] for j in range(n1+1) ] 
        dp[0][0] = True
        for i in range(1,n1+1) :
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1] 
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1] 
        print dp
        for i in range(1,n1+1): 
            for j in range(1,n2+1) : 
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j -1 ]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        
        return dp[n1][n2]