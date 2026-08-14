class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True

        a=(len(nums)//2)
        med=nums[a]
        d={}
        for k in nums:
            d[k]=nums.count(k)
        
        value=d.get(med)
        
        if value==1:
            return True
        if value>1:

            return False
            

        