class Solution(object):
    def fullJustify(self, words, L):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(words):
            left = i; size = 0
            while i < len(words) :
                if size == 0:
                    newsize = len(words[i])
                else:
                    newsize = size + len(words[i]) + 1
                if newsize <= L: 
                    size = newsize
                else: 
                    break 
                i += 1
            spaceCnt = L - size 
            if i - left - 1 > 0 and i < len(words) :
                spaceForEachCnt = spaceCnt / ( i - left - 1)
                spaceCnt %= i - left - 1 
            else:
                ## only 1 word for a line, left adjustification
                spaceForEachCnt = 0 
                
            ## each line 
            j = left
            while j < i :
                if j == left: curr = words[j] 
                else:
                    curr += ' ' * (spaceForEachCnt + 1) 
                    if spaceCnt > 0 and i < len(words):
                        curr += ' ' 
                        spaceCnt -= 1
                    curr += words[j]
                j += 1
            
            curr += ' ' * spaceCnt # left adjust
            res.append(curr) 
        return res
                