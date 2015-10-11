class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        res = 0 
        if len(prices) < 2: return res
        hasStock = 0
        prev = prices[0]; pbuy = 0
        for i in range(1, len(prices)):
            if prices[i] > prev:
                if not hasStock: 
                    hasStock += 1
                    pbuy = prev
            elif prices[i] < prev: 
                if hasStock: 
                    hasStock -=1
                    res +=  prev - pbuy
                    pbuy = 0 
            prev = prices[i]
        return res +( prev - pbuy if hasStock else 0 )

            
        