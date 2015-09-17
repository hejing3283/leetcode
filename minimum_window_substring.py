class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        cntDict = {}
        for i in t: 
            if i not in cntDict: cntDict[i] = 1
            else:  cntDict[i] += 1 
        
        cnt = len(t) 
        start = 0 ;
        minSize = 100000; 
        minStart = 0
        for end in range(len(s)):
            if s[end] in cntDict :
                cntDict[ s[end] ] -= 1
                if cntDict[ s[end] ] >= 0 :
                    cnt -= 1 
            if cnt == 0 :
                while True:
                    if s[start] in cntDict:
                        if cntDict[ s[start] ] < 0 :
                            cntDict[ s[start] ] += 1
                        else :
                            break
                    start += 1
                if minSize > end - start + 1:
                    minSize = end - start + 1
                    minStart = start 
        if minSize == 100000: 
            return ''
        else : 
            return s[minStart : (minStart + minSize)] 