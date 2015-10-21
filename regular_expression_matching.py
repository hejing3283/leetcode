class Solution(object):
    def isMatch_recursive(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0: return len(s) == 0
        if len(p) == 1 or p[1] != '*':
            if len(s) ==0 or ( s[0] != p[0]) and p[0] != ".":
                return False 
            return self.isMatch(s[1:], p[1:])
        else:
            i = -1; length = len(s)
            while i < length and (i <0 and p[0] == '.' or p[0] == s[i]):
                if self.isMatch(s[i+1:], p[2:]): return True
                i+=1
            return False
    def isMatch(self, s, p):
        ### if p[i+1] != "*" if p[j] == s[i] ==> match( s[i+1], p[j+1] ), if p[j] != s[i] == > return False
        ### if p[j+1] == "*" if p[j] == s[i] ==> match( s[i+1], p[j+2] ), match(s[i], p[j+2]), 
        ###                  if p[j] != s[i] == > match(s[i], p[j+2]) 
        
        if len(p) ==0 : return len(s) == 0 
        dp = [ [ False for _ in range(len(p) + 1)] for __ in range(len(s) + 1) ]
        dp[0][0] = True 
        for i in range(1, len(p) + 1):
            if p[i-1] == "*":
                if i >= 2: dp[0][i] = dp[0][i-2]
                    
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == ".": 
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "." ) )
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[len(s)][len(p)]
        