class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2: return 0 
        res = 0
        nday = len(prices) 
        pmin = prices[0] 
        
        for i in range(1,nday):
            if prices[i] < pmin: pmin = prices[i]
            if prices[i] - pmin > res: res =  prices[i] - pmin
        return res
        