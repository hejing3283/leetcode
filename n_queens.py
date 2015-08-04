class Solution:
  # @param {integer} n
  # @return {string[][]}
  def solveNQueens(self, n):
    if n < 1 or n == 2 or n == 3: return [[]]
    if n == 1: return [['Q']]

    return ans 


sol = Solution()
print [[".Q..",  "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
print sol.solveNQueens(4)
print sol.solveNQueens(8)

