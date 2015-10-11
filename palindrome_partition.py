class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ### method 1 : dfs 
        def isPalindrome( s ) :
            if not s: return False 
            i = 0 ; j = len(s) -1
            while i<j:
                if s[i] != s[j]: return False 
                i += 1; j -= 1
            return True
        def dfs( s, vallist) : 
            if len(s) == 0 : res.append(vallist) 
            for i in range(1,len(s)+1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], vallist + [s[:i]])  
                    
        res = []
        dfs(s, []) 
        return res
        
        