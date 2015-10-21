class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern: return False 
        strs = str.split(" ");
        if len(strs) != len(pattern): return False
            
        charMap = dict(); strMap = dict()
        for i in range(len(pattern)):
            char = pattern[i]; ss = strs[i]
            if not charMap.get(char,None):
                charMap[char] = ss
            if not strMap.get(ss,None):
                strMap[ss] = char 
            if charMap.get(char,None) != ss or strMap.get(ss,None) != char:
                return False
        return True 
                