class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start=0
        end=len(arr)
        ans=0
        while start<=end:
            mid=(start+end)/2
           
            if arr[mid]<arr[mid+1]:
                start=start+1
            else:
                 
                ans=mid
                end=mid-1
        return ans
        