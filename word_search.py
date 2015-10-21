class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if not board : return False 
        nrow = len(board) 
        ncol = len(board[0])
        
        for x in range(nrow):
            for y in range(ncol): 
                res = self.dfs(board, nrow, ncol, x, y, word ) 
                if res : 
                    return True 
        return False 
    def dfs(self, board, nrow, ncol, x, y, word):
        # print x, y, i 
        if len(word) == 0: return True 
        if x < 0 or x >= nrow or y < 0 or y >=ncol or board[x][y] != word[0]:return False 
        tmp = board[x][y] 
        board[x][y] = "#"
        ans =  self.dfs(board, nrow, ncol, x+1, y, word[1:])  or \
                         self.dfs(board, nrow, ncol, x-1, y, word[1:]) or \
                         self.dfs(board, nrow, ncol, x, y-1, word[1:]) or \
                         self.dfs(board, nrow, ncol, x, y+1, word[1:]) 
        board[x][y] = tmp
        return ans 
        