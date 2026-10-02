class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)-1
        ans=len(nums)
        i=0
        while i<=n:
            mid=(i+n)//2
            if nums[mid]>=target:
                ans=mid
                n=mid-1
            else:
                i=mid+1
        if ans ==len(nums) or nums[ans] != target:
            return [-1, -1]
        n=len(nums)-1
        ans1=len(nums)
        i=0
        while i<=n:
            mid=(i+n)//2
            if nums[mid]>target:
                ans1=mid
                n=mid-1
            else:
                i=mid+1
        return [ans,ans1-1]
            
    
