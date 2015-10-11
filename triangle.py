class Solution(object):
    def minimumTotal(self, T):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not T: return 0
        if len(T) == 1: return min(T[0])
        
        prev = T.pop(0)
        while T:
            tmp = T.pop(0)
            cur = [0 for _ in range(len(tmp))]
            cur[0] = prev[0] + tmp[0]; i = 1
            while i < len(prev) :
                cur[i] = ( min(prev[i], prev[i-1]) + tmp[i] )
                i += 1
            cur[i] = tmp[i] + prev[-1]
            print prev, "\t", cur 
            prev = cur 
        return min(cur) 
                
        