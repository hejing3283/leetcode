class Solution:
  # @param {integer} n
  # @return {integer}
  def totalNQueens(self, n):
    def is_QkinColumnJ(k, j ):
      for i in range(k):
	if board[i] == j or abs(k - i) == abs(board[i] - j) :
	  return False
      return True

    ans = 0; 
    board  = [-1 for _ in range(n)]
    row = 0; col = 0
    while row < n:
      while col < n:
	if is_QkinColumnJ(row, col):
	  board[row] = col 
	  col = 0
	  break
	else:
	  col += 1
      if board[ row ] == -1:
	if row == 0:
	  break
	else:
	  row -= 1
	  col = board[row] + 1
	  board[ row ] = -1
	  continue 
      if row == n-1:
	ans += 1
	col = board[row] + 1
	board[row] = -1
	continue 
      row += 1
    return  ans

sol = Solution()
print sol.totalNQueens(4)
# print sol.totalNQueens(8)

