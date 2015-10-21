class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 : return 1
        i2 = i3 = i5 = 0
        dp = []
        dp.append(1)
        while len(dp) < n : 
            m2, m3, m5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            dp.append(m)
        return dp[n-1]
        
        
    # def isUgly( self, num) :
    #     if num % 3 ==0 or num % 5 == 0 or num%2 == 0: return True
    #     return False 
    