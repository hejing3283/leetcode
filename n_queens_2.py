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
    depth = 0; curr = []
    while depth < n :


      
    return 
