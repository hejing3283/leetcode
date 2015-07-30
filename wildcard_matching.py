def isMatch(s, p):
  curS = 0 ; curP = 0
  star = 0; ss = s[::] 
  while curS < len(s) and curP < len(p):
    print curS, curP, star,
    if p[curP] == "*":
      print 'case 1' 
      star = curP; ss = s[curS::]; curP += 1
      continue
    if p[curP] == '?' or s[curS] == p[curP] : 
      print 'case 2' 
      curS += 1 ; curP += 1
      continue
    if star: 
      print 'case star' 
      curP = star + 1
      curS += 1
      s = ss[curS::]
      continue
    return False

  if p[curP-1] == "*" : return True
  if p[curP-1] == s[curS-1:]: return True 
  return False 
  

# print  isMatch("aa","a")      ," False "  
# print  isMatch("aa","aa")     ," True  "
# print  isMatch("aaa","aa")    ," False "
# print  isMatch("aa", "*")     ," True  "
# print  isMatch("aa", "a*")    ," True  "
# print  isMatch("ab", "?*")    ," True  "
# print  isMatch("aab", "c*a*b")," False "
# print  isMatch("abed", "?b*d**")," True "
# print  isMatch("abefcdgiescdfimde", "ab*cd?i*de")," True "
print  isMatch("", "")," True "
