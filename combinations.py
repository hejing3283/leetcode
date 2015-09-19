class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs( start, valueList) : 
            if self.count == k : self.ret.append(valueList); return
            else:
                for i in range(start, n + 1 ):
                    self.count += 1
                    dfs( i+1, valueList + [i] )
                    self.count -= 1
                
        self.ret = [] ; self.count = 0
        dfs(1,[])
        return self.ret
        