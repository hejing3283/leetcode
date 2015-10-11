class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s) 
        if lens < 2: return 0 
        flag = [ [ False for i in range( lens )  ] for j in range(lens) ] 
        # flag = [ [ True if i == j else False for i in range( lens )  ] for j in range(lens)] 
        
        cnt = [ len(s) - i  for i in range(lens+1)]

        for i in range(lens-1, -1, -1) :
            for j in range(i, lens): 
                if  s[i] == s[j] and (((j - i) < 2) or flag[i+1][j-1]): 
                    flag[i][j] = True
                    cnt[i] = min( cnt[j+1] + 1, cnt[i]) 
        print cnt
        return cnt[0] - 1 