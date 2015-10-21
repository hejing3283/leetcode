class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return self.method2_onlogn(citations)
        # return self.method1_on(citations)

        
    def method2_onlogn(self, citations) :
        ### slower then method 1 
        if not citations: return 0
        
        citations.sort(reverse = True)
        n = len(citations)
        ans = 0 
        for i in range(n):
            if citations[i] > i : 
                ans += 1 
        return ans 
    def method1_on(self, citations):
        if not citations: return 0 
        n = len(citations) 
        
        counts = [ 0 for _ in range(n+1)] 
        for i in citations:
            counts[ n if i > n else i] += 1 
            
        ans = 0 
        for h in range(n,-1,-1):
            ans += counts[h] 
            if ans >= h:
                return h
                
    
        
            
        