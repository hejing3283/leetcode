class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        ### TLE 
        # def dfs(s, wd) : 
        #     if s in wd: return True 
        #     else:
        #         for i in range(1,len(s)):
        #             if s[:i] in wd:
        #                 if s[i:] in wd : return True 
        #                 dfs(s[i:], wd)
        #         return False    
                    
        # if not wordDict and s: return False
        
        # return dfs(s, wordDict)
        
        ### DP    
        if (not s  and wordDict) or (s and not wordDict): return False
        n  = len(s) 
        dp = [False for i in range(n+1) ]; dp[0] = True
        for i in range(1, n+1): 
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: 
                    dp[i] = True
                    
        return dp[n]
        