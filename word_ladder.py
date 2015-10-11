class Solution(object):
    def ladderLength(self, startw, endw, wdict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wdict.add( endw )  ## set use add
        q = []
        q.append((startw,1))
        while q:
            curr = q.pop(0)
            currw = curr[0]; currlen = curr[1]
            if currw == endw: return currlen
            
            for i in range(len(startw)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    wleft = currw[:i]; wright = currw[(i+1):]
                    if currw[i] != j : 
                        tmp = wleft + j + wright
                        if tmp in wdict:
                            q.append( (tmp, currlen + 1) ) 
                            wdict.remove(tmp) 
        return 0
            