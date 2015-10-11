class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1: return 1 
        candy = [ 1 for i in range(n)]
        for i in range(1,n): 
            if ratings[i] > ratings[i-1] : candy[i] = candy[i-1] + 1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1] : candy[i] = max(candy[i+1] + 1, candy[i])
        return sum(candy)
            