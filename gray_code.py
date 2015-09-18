class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = 1 << n 
        res = []
        for i in range(size):
            res.append( ( i >> 1) ^ i ) 
        return res
                