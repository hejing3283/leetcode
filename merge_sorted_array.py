# class Solution(object):
#     def merge(self, A, m, B, n):
        # """
        # :type nums1: List[int]
        # :type m: int
        # :type nums2: List[int]
        # :type n: int
        # :rtype: void Do not return anything, modify nums1 in-place instead.
        # """
        # tmp = []
        # A.sort()
        # B.sort()
        # p1 = 0; p2 = 0 ; 
        # while p1 < m and p2 < n :
        #     if A[p1] > B[p2]:
        #         tmp.append(B[p2])
        #         p2 += 1
        #     else:
        #         tmp.append(A[p1])
        #         p1 += 1
        # if p1 < m :
        #     tmp.extend(A[p1:])
        # elif p2 < n:
        #     tmp.extend(B[p2:])
        # A[:] = tmp[::]
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()    
            