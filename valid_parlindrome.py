def isPalindrome( s):
  if s:
    p1 = 0; p2 = len(s)-1
    while p1 < p2:
      while p1 < p2 and not (s[p1].isalpha() or s[p1].isdigit()):
        p1 += 1
      while p1 < p2 and not (s[p2].isalpha() or s[p2].isdigit()):
        p2 -= 1
      if s[p1].lower() != s[p2].lower():
        return False
      p1 += 1
      p2 -= 1
    return True  
  else:
    return True
print isPalindrome("A man, a plan, a canal: Panama")
print isPalindrome("la2al")
print isPalindrome("x2")


