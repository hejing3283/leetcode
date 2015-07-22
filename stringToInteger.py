def myAtoi(s):
  '''
  1. empty ==> 0
  2. leading or tailing space
  3. overflow == 2147483647, underflow = -2147483648 
  '''
  s = s.strip()
  if not s:
    return 0
  iout = []
  isign = [] 
  for i in s :
    if (i == '+' or i == '-') and len(iout) == 0 :
      isign.append(i)
    elif i.isdigit():
      if i == '0' and len(iout) ==0:
	continue
      iout.extend(i)
    else:
      break
  if len(iout) == 0:
    return 0
  elif len(isign) > 1:
    return 0
  else:
    out = int("".join(isign +  iout))
    if out > 2147483647:
      return 2147483647
    elif out < -2147483648:
      return -2147483648
    else:
      return out
print -345, myAtoi("  -345c")
print 0, myAtoi("abc")
print 0, myAtoi("+-2")
print 12, myAtoi("+12ac2")
print 2147483647, myAtoi("124596739023")

