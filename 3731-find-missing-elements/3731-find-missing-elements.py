class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nu=[]
        nums.sort()
        Max=max(nums)
        Min=min(nums)
        for i in range(Min,Max):
            if i in nums:
                pass
            if i not in nums:
                nu.append(i)
        if len(nums)!=0:
            return nu
        else:
            return nu
       
        