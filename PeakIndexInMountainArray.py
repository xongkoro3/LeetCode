class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        startpoint = 0
        endpoint = len(A)
        if len(A) == 1:
            return 0
        while startpoint <= endpoint:
            midpoint = startpoint+(endpoint - startpoint)/2
            if A[midpoint] > A[midpoint+1] and  A[midpoint] > A[midpoint-1]:
                return midpoint
            elif A[midpoint] <= A[midpoint+1]:
                startpoint = midpoint
            elif A[midpoint] <= A[midpoint -1]:
                endpoint = midpoint
