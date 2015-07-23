def longestPalindrome(s):
  '''
  maximum length of s is 1000, unique solution
  '''
  istart = 0; iend = 0
  for i in range( len(s) ) :
    len1 = extendAroundCenter( s, i, i )
    len2 = extendAroundCenter( s, i, i + 1 )
    lenMax = max( len1, len2 )
    if lenMax > iend - istart :
      print i, istart, iend
      istart = i - (lenMax - 1 ) / 2 
      iend = i + lenMax/2 
  return s[istart:(iend+1)]
def extendAroundCenter(s, left,right):
  pL = left; pR = right
  while pL >= 0 and pR <= len(s)-1:
    if s[pL] == s[pR] :
      pL -= 1
      pR += 1
    else:
      break
  return (pR -1) - (pL +1) + 1 

print longestPalindrome("abcb")
print longestPalindrome("")
