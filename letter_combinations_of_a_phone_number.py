class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        numMap = dict(zip([str(i) for i in range(10)], [' ','*', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']))
        ans = []; 
        def dfs( digits, curr ) :
            if len(digits) == 0: 
                ans.append(curr); 
                return 
            else:
                if numMap[digits[0]]:
                    for s in numMap[digits[0]]:
                        dfs( digits[1:], curr + s ) 
                else:
                    dfs(digits[1:], curr ) 
        
        dfs(digits, '')
        return ans