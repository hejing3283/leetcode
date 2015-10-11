class Solution(object):
    def findLadders(self, startw, endw, wdict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        ### 2 q, one for prevMap, one for currq
        
        wdict.add(endw)
        prevMap = {}; 
        for i in wdict: prevMap[i] = []
        result = [] 
        qcurr= set(); qprev=set(); wlen = len(startw)
        qcurr.add(startw)
        while True:
            qcurr, qprev = qprev.copy(), qcurr.copy()
            for i in qprev: wdict.remove(i) ## use only once
            qcurr.clear() 
            for currw in qprev: 
                for i in range(wlen):
                    wl = currw[:i]; wr = currw[(i+1):]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if currw[i] != j: 
                            nextw = wl + j + wr
                            if nextw in wdict:
                                prevMap[nextw].append(currw)
                                qcurr.add(nextw) 
            if len(qcurr) == 0 : return result
            if endw in qcurr: break
                      
        def dfs(path, word ) :
            if  not len(prevMap[word]) : 
                path.append(word); currPath = path[:]
                currPath.reverse()
                result.append(currPath) 
                path.pop()
                return 
            path.append(word)
            for w in prevMap[word]:
                dfs(path, w)
            path.pop()
        dfs([], endw) 
        return result 
        
        
        ### fail
        # def dfs( startw, endw, wdict, curr, res) :
        #     if startw == endw: 
        #         res.append( curr ) ;
        #         return 
        #     for i in range(len(startw)):
        #         wl = startw[:i]; wr = startw[(i+1):]
        #         for j in 'abcdefghijklmnopqrstuvwxyz':
        #             if startw[i] != j:
        #                 wtmp = wl + j + wr 
        #                 if wtmp in wdict:
        #                   return dfs(wtmp, endw, wdict, curr + [wtmp], res)
        # res = []
        # wdict.add(endw)
        # dfs( startw, endw, wdict, [], res) 
        # return res
            
                                
                            