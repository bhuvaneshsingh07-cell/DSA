class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=len(nums)
        nums.sort()
       
        Max1=nums[b-1]*nums[b-2]*nums[b-3]
        Max2=nums[0]*nums[1]*nums[b-1]
        res=max(Max1,Max2)
        return res
        
           