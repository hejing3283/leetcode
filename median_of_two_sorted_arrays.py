class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ### The median is also the number that is halfway into the set
        m = len(nums1) ; n = len(nums2) ; totalLen = m + n 
        if  (totalLen - 1) % 2:  
            return (self.method2( nums1, m, nums2, n, (totalLen)/2 ) + self.method2( nums1,m,nums2, n,(totalLen)/2 + 1) ) / 2.0  
        else:
            return self.method2( nums1,  m, nums2, n, (totalLen/2 + 1))
            
        # return self.method1(nums1,nums2) 
        
    def method1(self,nums1, nums2):
        ### merge and median 
        ### very fast beat 98% of python submission
        if not nums1 and not nums2 : return 0 
        nums = nums1 + nums2 ; nums.sort()
        n = len(nums) - 1 
        return ( nums[ n / 2] + nums[ n/2 + n%2] ) /2.0
    
    def method2( self, nums1,  m,nums2, n, k):
        ### 核心是将原问题转变成一个寻找第k小数的问题（假设两个原序列升序排列），
        ### 这样中位数实际上是第(m+n)/2小的数。所以只要解决了第k小数的问题，原问题也得以解决。
        if m > n : m, n = n, m ;  nums1, nums2 = nums2, nums1
        if not m: 
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0]) 
            
        p1 = min( k / 2, m) ; p2 = k - p1 
        if nums1[p1-1] < nums2[p2 -1] :
            return self.method2( nums1[p1:], m - p1, nums2, n ,k-p1)
        elif nums1[p1-1] > nums2[p2-1]:
            return self.method2( nums1, m, nums2[p2:], n-p2, k-p2)
        else:  
            return nums1[p1-1]
