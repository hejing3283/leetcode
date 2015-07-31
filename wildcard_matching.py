def isMatch(s, p):
  curS = curP = ss = 0;  star = -1;  
  while curS < len(s) :
    if curP < len(p) :
      if p[curP] == '?' or s[curS] == p[curP] : 
      	curS += 1 ; curP += 1; continue
    if curP < len(p) :
      if p[curP] == "*" :
	star = curP;  curP += 1; ss = curS; continue
    if star != -1 : 
      curP = star + 1;  ss += 1; curS = ss; continue
    return False
  
  while curP < len(p) and p[curP] == "*": curP += 1 
  if curP == len(p) : return True
  return False 
  

print  isMatch("aa","a")      ," False "  
print  isMatch("aa","aa")     ," True  "
print  isMatch("aaa","aa")    ," False "
print  isMatch("aa", "*")     ," True  "
print  isMatch("aa", "a*")    ," True  "
print  isMatch("ab", "?*")    ," True  "
print  isMatch("aab", "c*a*b")," False "
print  isMatch("abed", "?b*d**")," True "
print  isMatch("abefcdgiescdfimde", "ab*cd?i*de")," True "
print  isMatch("", "")," True "
print  isMatch("", "a")," False "
print  isMatch("", "*")," True "
print  isMatch("", "?")," False "
print  isMatch("a", "a*")," True "
print  isMatch("a", "aa")," False "
print  isMatch("a", "?")," True "
print  isMatch("a", "*")," True "
print  isMatch("a", "")," False "
print  isMatch("a", "?*")," True "
print  isMatch("a", "?a*")," False "
print  isMatch("a", "a?")," False "
print  isMatch("a", "??")," False "
print  isMatch("a", "**")," True "
print  isMatch("a", "*?*")," True "
print  isMatch("a", "?*?")," False "
