class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        n = len(nums)
        sums = [ [nums[i] + nums[j], j, i] for i in xrange(n) for j in xrange(i) ] 
        res, d = set(), collections.defaultdict(list)
        for n in sums :
            t2 = target - n[0]
            if t2 in d:
                for ls in d[t2]:
                    t2_list = set(ls[1:] + n[1:])
                    if len(t2_list) == 4 :
                        t2_list = [nums[idx] for idx in t2_list]
                        t2_list.sort()
                        res.add( tuple(t2_list) )
            d[n[0]].append(n)
        
        return list(res)
    
        
            
    
            
                
            