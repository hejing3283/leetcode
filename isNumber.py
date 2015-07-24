def isNumber(s):
  '''
  '''
  MAX = 2147483648
  MIN = -2147483648
  def str2int(s):
    s = s.strip()
    n = len(s)
    sint = ''; sdec = '' ; sign = 1; join = ''
    i = 0;
    if s[i] == '+' and i < n :
      sign = 1 
      i += 1
    elif s[i] == '-' and i < n :
      sign = -1
      i += 1
    num = 0
    while i < n and s[i].isdigit():
      d = int(s[i])
      if num > MAX or ( num == MAX and d > 8 ):
         return  MAX if sign == 1 else MIN
      num = num * 10 + d 
      i += i 

    return(sign * num)
  
  s = s.strip()
  n = len(s)
  i = 0 
  dec = ''
  while i < n and (s[i].isdigit() or s[i] == "." or s[i].lower() == 'e'):
    i = i + 1
      

  # decimal

  # scientifi
  
  return isNum


s = "0"	   , print "true", isNumber(s)  
s = " 0.1 ", print "true", isNumber(s)
s = "abc"  , print "fals", isNumber(s)
s = "1 a"  , print "fals", isNumber(s)
s = "2e10" , print "true", isNumber(s)

