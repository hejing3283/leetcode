class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #### Time limit excess
        # def maxDay( P ) :
        #     if len(P) < 2: return ( 0  ) 
        #     prev = P[0]; hasStock = 0 ; 
        #     pft = 0 
        #     for i in range(1,len(P)):
        #         if P[i] > prev and not hasStock: 
        #             pbuy = prev; hasStock += 1 
        #         elif P[i] < prev and hasStock: 
        #             hasStock -= 1
        #             pft += prev - pbuy
        #         prev = P[i]
        #     return pft + ( prev - pbuy if hasStock else 0 )
           
        # res = 0
        # if len(prices) < 2: return res
        # for i in range(len(prices)):
        #     res = max( maxDay( prices[:i]), maxDay( prices[i:]))

        # return res
        
        #### Methods 2 
        res = 0 
        if len(prices) < 2: return res 
        
        f1 = [ 0 for _ in prices ] ; f1[0] = 0 
        minV = prices[0]
        for i in range( 1, len(prices) ):
            minV = min(minV, prices[i]) 
            f1[i] = max( f1[i-1], prices[i] - minV)
        
        f2 = [ 0 for _ in prices ] ; f2[-1] = 0 
        maxV = prices[-1]
        for i in range(len(prices)-2, -1, -1 ) : 
            maxV = max( prices[i], maxV) 
            f2[i] = max( f2[i+1], maxV - prices[i] ) 
        
        for i in range(len(prices)): 
            res = f1[i] + f2[i] if f1[i] + f2[i] > res else res
        return res
            
        
            
            