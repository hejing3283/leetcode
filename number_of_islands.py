class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not len(grid): return ans
        m = len(grid); n = len(grid[0])
        visited = [ [False for _ in range(n)] for _ in range(m)]    
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and not visited[x][y]:
                    ans +=1
                    # self.bfs( grid, visited, m, n, x, y)
                    self.dfs( grid, visited, x, y, m, n) 

        return ans
     
    def bfs(self, grid, visited, m, n, x, y):
        queue = [(x, y)] 
        visited[x][y] = True
        out = zip([1,0,-1,0],[0,1,0,-1])
        while queue:
            edge = queue.pop(0)
            for p in out:
                i = edge[0] + p[0];  j = edge[1] + p[1]
                if self.isValidLoc([i,j],m, n) and grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    queue.append([i,j])

    def dfs(self, grid, visited, x, y, m, n):
        visited[x][y] = True
        if self.isValidLoc([x-1,y],m,n) and grid[x-1][y] == '1' and not visited[x-1][y]:
            self.dfs(grid,visited, x-1, y,m,n)
        if self.isValidLoc([x+1,y],m,n) and grid[x+1][y] == '1' and not visited[x+1][y]:
            self.dfs(grid,visited, x+1, y,m,n)
        if self.isValidLoc([x,y-1],m,n) and grid[x][y-1] == '1' and not visited[x][y-1]:
            self.dfs(grid,visited, x, y-1,m,n)
        if self.isValidLoc([x,y+1],m,n) and grid[x][y+1] == '1' and not visited[x][y+1]:
            self.dfs(grid,visited, x, y+1,m,n)
        
    def isValidLoc( self, loc, m, n ) :
        # is a valid position on the grid?
        return loc[0] >= 0 and loc[0] < m and loc[1] >= 0 and loc[1] < n 