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
            
            if i not in nums:
                nu.append(i)
        return nu