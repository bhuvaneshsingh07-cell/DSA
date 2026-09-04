class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Max=[]
        Min=nums[:]
       
      
        diff=0
        
        for i in range(len(nums)):
            #for max
            Max.append(nums[i])
            m=max(Max)
        
            #for min 
            mi=min(Min)
            Min.remove(nums[i])


            
            
        

            #for diff 
            diff=m-mi
            if diff<=k:
              
                return i
        return -1