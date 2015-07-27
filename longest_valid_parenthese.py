def longestValidParentheses(s):

  match = [ False for _ in s ]
  pStack = []

  for i in range(len(s)):
    if s[i] == "(":
      pStack.extend([i])
    elif s[i] == ")" and pStack:
      match[i] = True
      match[pStack.pop()] = True
  maxLen = 0; currLen = 0
  for i in range(len(match)):
    if match[i]  == True:
      currLen += 1
    else:
      maxLen = max(currLen, maxLen) 
      currLen = 0
  maxLen = max(currLen, maxLen) 
  return maxLen

print "0", longestValidParentheses(")")
print "0", longestValidParentheses("")
print "6", longestValidParentheses("((()))")
print "4", longestValidParentheses(")()()")
print "2", longestValidParentheses("(()")
