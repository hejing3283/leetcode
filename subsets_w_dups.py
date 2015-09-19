class Solution(object):
    def subsetsWithDup(self, N):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs( depth, start, valueList ) :
            if valueList not in res : res.append( valueList ) 
            if depth == len(N) : return 
            for i in range( start, len(N) ) :
                dfs(depth + 1, i+1, valueList + [N[i]] ) 
        N.sort()
        res = []
        dfs(0,0,[])
        return res