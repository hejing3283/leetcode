


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0 : n /= 4
        
        if ( n % 8 == 7 ): return 4
        
        a = 0 
        while a * a <=n: 
            b = int( math.sqrt( n - a*a)  ) 
            if  a*a + b*b == n :
                return ( 2 if (a >0 and b>0 )else 1)
            a += 1
        return 3 
        
        
        #### DP1, TLE 5723 fail
        # INT_MAX = n + 1
        # dp = [ INT_MAX for i in range(n+1) ] 
        # dp[0] = 0 
        # for i in range(n+1):
        #     j = 1 
        #     while i + j*j <=n:
        #         dp[ i + j*j ]  = min(dp[i + j*j], 1 + dp[i])
        #         j += 1
        # return dp[-1]
        
        #### recursion 9756 fail 
        # ### TLE
        # import math
        # ans, num = n, 2
        # while num*num <= n:
        #     tmp = (num*num)
        #     a = n / tmp; b = n % tmp            
        #     ans = min( ans, a + self.numSquares(b))
        #     num += 1 
        # return ans