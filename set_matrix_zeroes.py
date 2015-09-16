class Solution(object):
    def setZeroes(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(M[0]) ; m = len(M) 
        rows = []; cols = []
        i = 0; 
        while i < m :
            j = 0
            while j < n :
                if M[i][j] == 0 :
                    rows.append(i)
                    cols.append(j)
                j += 1; 
            i += 1
        print rows, cols
        for i in list(set(rows)) :
            for jj in range(n): 
                print i, jj
                M[i][jj] = 0
        for j in list(set(cols)) :
            for ii in range(m):
                M[ii][j] = 0
        