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
    intv.sort(key = lambda x:x.start )

    ## find boundaries
    ss = [ intv[i].start for i in range(len(intv)) ] 
    sleft, sright = self.bSearch( 0, len(intv) -1, ss, newIntv.start )  
    ee = [ intv[i].end for i in range(len(intv)) ] 
    eleft, eright = self.bSearch( sleft, len(intv) -1, ee, newIntv.end )  

    ## output 
    return intv 

  def bSearch( self, left, right, nums, val ) :
    med = (left + right ) / 2 
    if right - left > 1:
      if val < nums[ med ] : return self.bSearch(left, med , nums, val ) 
      elif val > nums[ med ] : return self.bSearch(med ,right, nums, val ) 
      else: return left, left + 1

    else: 
      if val <= nums[ left ] : return 0, 0  
      if val >= nums[ right ] : return right, right
    return left, right 



s = Solution()
intv = [ Interval(1,3),Interval(6,9) ] 
newIntv = Interval(2,5)
res = s.insert(intv, newIntv) 
#as [1,5],[6,9] 
for i in range(len(res)):
  print "[", res[i].start,",", res[i].end, "]", 
  

# # [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
intv = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10), Interval(12,16) ]
newIntv = Interval(4,9)

res = s.insert(intv, newIntv) 
for i in range(len(res)):
  print "[", res[i].start,",", res[i].end, "]", 
  

