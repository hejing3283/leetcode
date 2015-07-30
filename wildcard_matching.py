def isMatch(s, p):
  if p[0] == "*":
    if len(p) == 1: return True
    else : isMatch(s[::], p[1::])
  elif p[0] == '?':
    if len(p) == 1: return True
    else: isMatch(s[1::], p[1::])
  else:
    for i in range( len(s)):
      if s[i] == p[0] :
        if len(p) > 1:
	  isMatch(s[i+1::], p[1::])
        else:
          return True
      else:
	return False
    return False


print  isMatch("aa","a")      ," false "  
print  isMatch("aa","aa")     ," true  "
print  isMatch("aaa","aa")    ," false "
# print  isMatch("aa", "*")     ," true  "
print  isMatch("aa", "a*")    ," true  "
print  isMatch("ab", "?*")    ," true  "
# print  isMatch("aab", "c*a*b")," false "
