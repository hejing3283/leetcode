class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        ops = { '+': lambda x,y : x + y,
                '-': lambda x,y : (x) - (y), 
                '*': lambda x,y : x * y,
                '/': lambda x,y : int( float(x) / y),  } ## python integer division problem
        stack = []
        for t in tokens:
            if t in ops:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append( ops[ t ](n1, n2) )
            else:
                stack.append( int( t ) )
        return stack[0] 
                
            