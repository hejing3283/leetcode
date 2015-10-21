class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        ### 由于 k 的限制，使得决策之间产生了联系
        n = len(prices)
        if 2*k >= n:
            ### without this, it's going to reach memory limite
            ### greedy:
            ans = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
            return ans
            
        dp = [None] * (k * 2+1)
        dp[0] = 0
        for i in range(n):
            for j in range(1, min(2*k, i+1)+1):
                dp[j] = max(dp[j] , dp[j-1] + prices[i] * [1,-1][ j % 2] )
        return dp[2*k]
        