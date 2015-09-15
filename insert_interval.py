# Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class Solution(object):
  def insert(self, intv, newIntv):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    ## sort intv 
    intv.append(newIntv)
    intv.sort(key = lambda x:x.start )
    res = [intv[0]]
    for i in range(1, len( intv) ):
      if intv[i].start > res[-1].end:
	res.append( intv[i] ) 
      else:
	res[-1].start = min(intv[i].start, res[-1].start)
	res[-1].end = max( intv[i].end, res[-1].end) 
    return res


s = Solution()
intv = [ Interval(1,3),Interval(6,9) ] 
newIntv = Interval(2,5)
res = s.insert(intv, newIntv) 
#as [1,5],[6,9] 
for i in range(len(res)):
  print "[", res[i].start,",", res[i].end, "]", 

print "\n"

# # [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
intv = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10), Interval(12,16) ]
newIntv = Interval(4,9)

res = s.insert(intv, newIntv) 
for i in range(len(res)):
  print "[", res[i].start,",", res[i].end, "]", 
  

