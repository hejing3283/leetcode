def myAtoi(s):
  '''
  1. empty ==> 0
  2. leading or tailing space
  3. overflow == 2147483647 
  '''
  s = s.strip()
  if not s:
    return 0
  iout = []
  isign = ''
  for i in s :
    if (i == '+' or i == '-') and len(iout) == 0 :
      isign = i
    elif i.isdigit():
      if i == '0' and len(iout) ==0:
	continue
      iout.extend(i)
    else:
      continue
  if len(iout) == 0:
    return 0
  else:
    return int("".join([isign] +  iout))
print -345, myAtoi("  -345c")
print 0, myAtoi("abc")
print 2147483647, myAtoi("124596739023")

