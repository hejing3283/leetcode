class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) : return False 
        sMap = dict(); tMap = dict()
        for i in range(len(s)):
            ss = s[i]; tt = t[i]
            sMap[ss]  = 1 if not ss in sMap else sMap[ss] + 1
            tMap[tt]  = 1 if not tt in tMap else tMap[tt] + 1
                
        if len(sMap.keys()) != len(tMap.keys()): return False 
        
        for ks,ss in sMap.items():
            if ss != tMap.get(ks,None):
                return False 
        return True 
        