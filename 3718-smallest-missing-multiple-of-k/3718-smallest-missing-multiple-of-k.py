class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=len(nums)+2
        ash=[0]*l
        
        for i in range(1,len(nums)+2):
            ash[i]=k*i
        del ash[0]
       
      
        for i in ash:
            if i in nums:
                pass
            if i not in nums:
                return i
                

        