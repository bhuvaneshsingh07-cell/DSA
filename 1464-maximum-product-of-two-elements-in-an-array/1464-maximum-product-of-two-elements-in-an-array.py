class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max=[]
        a=nums.sort(reverse=True)
        d=(nums[0]-1)*(nums[1]-1)
        
        return d