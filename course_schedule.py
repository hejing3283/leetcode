class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ### run DFS first 
        degree = [ 0 for _ in range(numCourses)]
        map = [ [] for _ in range(numCourses)]
        
        for p in prerequisites:
            degree[p[0]] += 1 ### input are ints
            map[ p[1]].append( p[0] ) 
 
        ### topolocial sorting 
        st = []
        for i in range(numCourses):
            if degree[i] == 0 :
                st.append(i)
        
        count = 0 
        while st: 
            tmp = st.pop(0)
            count += 1
            for i in map[tmp] : 
                degree[i] -= 1
                if degree[i] == 0 :
                    st.append(i)
        
        return count >= numCourses
        