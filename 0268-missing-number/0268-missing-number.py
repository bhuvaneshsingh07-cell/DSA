class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sort=nums.sort()
        n=len(nums)
        
        for i in range(n):
            if nums[i]==i:
                pass
            if nums[0]!=0:
                return 0
            if nums[i]!=i:
                return i
        if nums[n-1]!=n:
            return n
            
            
           

        