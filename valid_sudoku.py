def isValidSudoku(b):
  # @param {character[][]} board
  # @return {boolean}
  def isValid(x,y,t):
    for i in range(9):
      if b[i][y] == t: return False
    for i in range(9):
      if b[x][i] == t: return False
    for i in range(3):
      for j in range(3):
	if b[x/3 * 3 + i][y/3 * 3 + j] == t: return False 
    return True

  for i in range(9):
    for j in range(9):
      if b[i][j] == '.': continue
      else :
	tmp = b[i][j]
	b[i][j] = 'D'
	if isValid(i, j, tmp) == False: 
	  return False
	else:
	  b[i][j] = tmp
  return True

b = [['5','3','.','.','7','.','.','.','.'],
     ['6','.','.','1','9','5','.','.','.'],
     ['.','9','8','.','.','.','.','6','.'],
     ['8','.','.','.','6','.','.','.','3'],
     ['4','.','.','8','.','3','.','.','1'],
     ['7','.','.','.','2','.','.','.','6'],
     ['.','6','.','.','.','.','2','8','.'],
     ['.','.','.','4','1','9','.','.','5'],
     ['.','.','.','.','8','.','.','7','9']]
print isValidSudoku(b) 
