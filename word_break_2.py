class Solution(object):
    def wordBreak(self, s, wdict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        ### 用一个字典将出现过的token记录下来，实现剪枝
        tokenMap  = {}
        def dfs(s):
            res = [] 
            if s in wdict: res.append(s)
            for i in range(len(s) - 1):
                prefix, suffix = s[:i+1], s[i+1:]
                if prefix not in wdict:
                    continue
                reminder = [] 
                if suffix in tokenMap:
                    reminder = tokenMap[ suffix ]
                else:
                    reminder = dfs(suffix) 
              
                for ss in reminder: 
                    res.append(prefix + " " + ss )
            tokenMap[ s ] = res
            return res
                
        return dfs(s) 
        
                
        
        ### TLE
        # def dfs(s, start, end, curr ) :
        #     if not s : curr = " ".join( curr) if len(curr) > 1 else curr; res.append( curr ); return 
        #     if s in wdict: res.append(s)
        #     for k in range(start, end) :
        #         if s[k:end] in wdict:
        #             dfs(s, start, k, curr + [s[k:end]])
        # res = []
        # dfs(s, 0, len(s), [])
        # return res
            