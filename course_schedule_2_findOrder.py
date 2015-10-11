class Solution(object):
    def findOrder(self, numC, prereq):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ind = [ 0 for _ in range( numC ) ] ## indegree
        myMap = [ [] for _ in range( numC) ] ## in nodes
        
        for p in prereq: 
            if p[0] not in myMap[p[1]] :
                ind[ p[0] ] += 1
                myMap[ p[1] ].append( p[0] )
        
        st = [] ### start nodes
        for c in range( numC ) : 
            if ind[c] == 0 : 
                st.append(c) 
                ind[c] = -1
            
        ans = []
        while st :
            tmp = st.pop(0)
            ans.append(tmp)
            for x in myMap[tmp]:
                ind[x] -= 1  
                if ind[x] == 0 :
                    st.append( x ) 
                    ind[ x ] = -1
        
        return ( ans if len(ans) >= numC else [])