class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # stmap = dict() ; ### version 0.0.3 delete
        ismap = dict(); itmap = dict()
        ####-----------
        if len(s) != len(t): return False
        
        n = len(s) 
        for i in range(n):
            ss = s[i]; tt = t[i]
            ###------ version 0.0.3 delete
            # if not ss in stmap:
            #     stmap[ss] = tt
            # elif stmap[ss] != tt:
            #     # print i, stmap[ss], tt
            #     return False 
            ####------------
            ismap[ss] = [i] if not ss in ismap else ismap[ss] + [i] 
            itmap[tt] = [i] if not tt in itmap else itmap[tt] + [i] 

        #### ------- version 0.0.1
        if len(ismap.keys()) != len(itmap.keys()) : return False 
        # for k, v in stmap.items():
        #     sid = ismap[k]; tid = itmap[v]
        #     if len(sid) != len(tid) : return False 
        #     else:
        #         for i in range(len(sid)):
        #             if sid[i] != tid[i]:
        #                 return False 
        # return True
        #### ---------
        ####--------- version 0.0.2 (replace v0.0.1)
        return sorted( ismap.values() ) == sorted( itmap.values() )
        ####----------
        
        # ####--------- version 0.0.3 (replace v0.0.2), slower then 0.0.2
        # is1 = ismap.values().sort(); it1 = itmap.values().sort()
        # return is1 == it1
        # ####----------

                    