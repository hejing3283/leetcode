def isMatch(s, p):
  pP = 0 ; pS = 0 
  while s:
    if p[0] == "*":
      while p[0] == "*": ip +=1
      p = p[ip-1:]
    elif p[0] == '?': 
      s = s[1:] ; 
      p = p[1:]
    else:
      if s[0] == p[0] : s = s[1:]; p = p[1:]
      else:

      for i in range( len(s)):
          if len(p) > 1:
	    s = s[i+1:]
	    p = p[1:]
            return isMatch(s, p)
          else:
            return True
        else:
	  return False
      return False
  

print  isMatch("aa","a")      ," false "  
# print  isMatch("aa","aa")     ," true  "
# print  isMatch("aaa","aa")    ," false "
# print  isMatch("aa", "*")     ," true  "
# print  isMatch("aa", "a*")    ," true  "
# print  isMatch("ab", "?*")    ," true  "
# print  isMatch("aab", "c*a*b")," false "
