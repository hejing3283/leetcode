def divide(dividend, divisor):
  sign = -1 if ( dividend > 0 ) + (divisor > 0 )== 1 else 1

  a = abs(dividend); b = abs( divisor );
  if ( a < b) : return 0
  currSum = 0;  count = 0; res = 0
  while b <= a:
    currSum = b
    count = 1
    while currSum + currSum  <= a :
      currSum += currSum
      count += count 
    a -= currSum
    res += count
  res = min(res, 2147483647)  if sign == 1 else  max(-res, -2147483648) 
  return res
print divide(100,2)
print divide(1010,-2)
print divide(101000000000,-0.5)
