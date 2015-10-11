class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t: return 1 
        if not s: return 0
        m = len(s) + 1; n = len(t) + 1
        if m == n : return int(s == t)
        
        dp = [ [ 0 for i in range(m)]  for j in range(n) ] 
        dp[0][:] = [ 1 for i in range(m) ] 
        dp[:][0] = [ 0 for j in range(n) ]
        dp[0][0] = 1
        for i in range(1, m) :
            for j in range(1, n):
                dp[j][i] = dp[j][i-1]  
                if s[i-1] == t[j-1]: 
                    dp[j][i] +=  dp[j-1][i-1]  
        return dp[n-1][m-1]


# class Solution:
#     # @return an integer
#     def numDistinct(self, S, T):
#         if len(S)==0:
#             return 0
#         if len(T)==0:
#             return 1### 
#         res=[0 for j in range(len(T)+1)]
#         res[0]=1
#         for  i in range(len(S)):
#             for j in reversed(range(len(T))):
#                 if S[i]==T[j]:
#                     res[j+1]=res[j]+res[j+1]
#         return res[len(T)]
                