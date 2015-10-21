# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len( points )
        if n < 3: return n 
        res = -1 
        for i in range(n):
            slope = {'Inf':0}
            samePoint = 1 
            for j in range(n):
                p1 = points[i]; p2 = points[j]
                if i == j :
                    continue
                elif p1.x == p2.x and p1.y != p2.y:
                    slope['Inf'] += 1
                elif p1.x != p2.x :
                    k = 1.0 * (p1.y - p2.y)/ (p1.x - p2.x ) 
                    if k not in slope: 
                        slope[k] = 1
                    else:
                        slope[k] += 1
                else:
                    samePoint += 1
            res = max(res, max(slope.values()) + samePoint) 
        
        return res 