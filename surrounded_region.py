class Solution(object):
    def solve(self, B):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        ###### method 2 bfs AC
        def fillD(irow, icol):
            if irow < 0 or irow > nrow-1 or icol < 0 or icol > ncol-1 or B[irow][icol] != 'O': return 
            queue.append( (irow,icol) )
            B[irow][icol] = 'D'

        def bfs( x, y ) :
            if B[x][y] == 'O': queue.append( (x,y)); fillD(x,y); 
            while queue:
                curr = queue.pop(); i = curr[0]; j=curr[1]
                fillD(i+1, j);  fillD(i-1, j); 
                fillD(i, j+1);  fillD(i, j-1) 
        
        if not B: return 
        nrow = len(B); ncol = len(B[0]); queue = []
        for i in range(nrow):
            bfs(i,0); bfs(i, ncol-1)
        for j in range(ncol):
            bfs(0,j); bfs(nrow-1, j)
            
        for i in range( nrow) :
            for j in range( ncol):
                if B[i][j] == 'O': B[i][j] ='X'
                elif B[i][j] == 'D': B[i][j] = 'O'
                   
        
        ###### method 1 dfs runtime error
        # if not B: return 
        # nrow = len(B)
        # ncol = len(B[0]) 
        
        # def dfs( irow, icol) : 
        #     if irow < 0 or irow > nrow-1 or icol < 0 or icol > ncol-1 or B[irow][icol] != 'O': return 
        #     B[irow][icol] = 'D'
        #     dfs( irow - 1,  icol) 
        #     dfs( irow + 1, icol)
        #     dfs( irow, icol - 1)
        #     dfs( irow, icol + 1) 
            
        # for i in range( nrow):
        #     dfs(i, 0); dfs(i, ncol-1)
        # for j in range(ncol):
        #     dfs(0, j); dfs(nrow-1, j)
        # for i in range( nrow) :
        #     for j in range( ncol):
        #         if B[i][j] == 'O': B[i][j] ='X'
        #         elif B[i][j] == 'D': B[i][j] = 'O'
                
        