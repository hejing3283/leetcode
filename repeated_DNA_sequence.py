class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.naiveSlidingWindow(s)
        
    def naiveSlidingWindow(self,s):
        n  = 10
        ans = []
        if len(s) <= 10: return ans
        myDict = {}
        for i in range(len(s)-n+1):
            ss = s[i:i+10]
            curr = myDict.get(ss,None) 
            if not curr: 
                myDict[ss] = 1 
            elif curr == 1: 
                myDict[ss] += 1
                ans.append(ss)
            
        return ans
                
        