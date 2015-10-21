class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
                
        ### optimize better, still have space
        if not n : return [[]]
        ans = [] ; N = n
        
        def dfs( n, k, curr, start ) :
            if k == 0 :
                if n != 0 : return
                else : ans.append(curr); return 
            if n < 0 or k < 0 or n < start: return  ### 提前剪枝
            for i in range(start,10):
                dfs( n - i , k - 1, curr + [i], i+1)
        dfs(n, k, [], 1)
        return ans
        
        
        # ### AC but slow
        # if not n : return [[]]
        # ans = [] ; N = n
        
        # def dfs( n, k, curr, start ) :
        #     if k == 0 :
        #         if n != 0 : return
        #         else : ans.append(curr); return 
        #     if n < start: return  ### 提前剪枝
        #     # if n < k * start: return 
        #     for i in range(start,10):
        #         dfs( n - i , k - 1, curr + [i], i+1)
        # dfs(n, k, [], 1)
        # return ans
        
        #### TLE
        # if not n : return [[]]
        # ans = [] ; N = n
        # def dfs( n, k, curr ) :
        #     if k == 0 :
        #         if n != 0 : return
        #         else : ans.append(curr); return 
        #     start = 1 if not curr else curr[-1]+1
        #     for i in range(start,10):
        #         dfs( n - i , k - 1, curr + [i])
        # dfs(n, k, [])
        # return ans