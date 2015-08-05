class Solution:
  # @param {integer} n
  # @return {string[][]}
  def solveNQueens(self, n):
    def isQinColumnI(k , j ):
      for i in range(k):
	if board[i] == j or abs( board[i] - j) == abs(i - k) :
	  return False
      return True

    def dfs(depth, curr ) :
      if depth == n: ans.append(curr) ; return 
      for i in range(n):
	if isQinColumnI( depth, i ):
	  board[ depth ]  = i 
	  s = '.'*n
	  dfs( depth + 1, curr + [s[:i] + 'Q' + s[i+1:]] )
    
    board = [ -1 for _ in range(n) ] 
    ans = []; 
    dfs(0, [])
    return ans 


sol = Solution()
print [[".Q..",  "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
print sol.solveNQueens(4)
print "---------------"
# print sol.solveNQueens(8)

