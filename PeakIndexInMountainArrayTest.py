from PeakIndexInMountainArray import Solution
A = [0,1,2,3,2,1]
B = [0,2,1,0]
C = [40,48,61,75,100,99,98,39,30,10]
if __name__ == '__main__':
    solution = Solution()
    ans = solution.peakIndexInMountainArray(C)
    print (ans)