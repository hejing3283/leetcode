def generateParenthesis(n):
  '''
  n = 3:
  "((()))", "(()())", "(())()", "()(())", "()()()"
  Thought:
  base: (), => in or out 
  induction: 
  '''
  def generate(p, lo, up, parens = [] ):
    if lo:  generate(p + '(', lo - 1, up )
    if up > lo :  generate(p + ')', lo, up - 1 )
    if not up : parens += p, 
    return parens
  return generate('', n, n ) 

print generateParenthesis(3)
print generateParenthesis(2)
    
       

		        
