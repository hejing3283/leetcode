# Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class Solution(object):
  def merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len( intervals  ) <= 1: return intervals
    intervals.sort( key = lambda x:x.start ) 
    
    res = [intervals[0] ] 
    for i in range( 1, len(intervals) ) :
      if intervals[ i ].start > res[-1].end or intervals[i].end < res[-1].start:
        res.append( intervals[i] )
      else :
        res[-1].start = min( intervals[i].start, res[-1].start)
        res[-1].end = max( intervals[i].end, res[-1].end)
    return res 

s = Solution()
intervals = [Interval(2,6),Interval(1,3),Interval(8,10),Interval(15,18)]
res = s.merge(intervals) 
for i in range(len(res)):
  print "[", res[i].start,",", res[i].end, "]", 
  

