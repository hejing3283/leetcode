# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         usually, to solve how many ? use dp
#         """
#         nDict = {}
#         for i in range(1,27):
#             nDict[str(i)] = 0
#         self.res = 0 

#         def dfs(depth, start ):
#             if depth == len(s) : self.res += 1 ; return 
#             for i in range(start, len(s) ) :
#                 if int( s[i] ) < 10 and int(s[i]) > 0 :
#                     dfs( depth + 1, i+1)
#                 else : 
#                     return self.res
#                 if int( s[i:i+2]) > 9 and in(s[i:i+1] < 26:
#                     dfs( depth + 2, i+2)
#                 else:
#                     return self.res
#         dfs(0,0)
#         return self.res
 
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        usually, to solve how many ? use dp
        """   
        n = len(s) 
        if not s or s[0] == '0' : return 0
        if n == 1: return 1 if s[0] !='0' else 0
        dp = [1,1]
        for i in range(2, n + 1) :
            curr = int( s[i-2:i] ) 
            if curr >= 10 and curr <= 26 and s[i-1] != '0': 
                    dp.append( dp[i-1] + dp[i-2] ) 
            elif curr == 10 or curr == 20:
                    dp.append( dp[i-2] )
            elif s[i-1] != '0' :
                dp.append( dp[i-1] ) 
            else :
                return 0 
        return dp[n]