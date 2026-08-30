class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1
        if len(nums)==2:
            return 2
        Max=0        
        Min=float('inf')
        indexmax=0
        indexmin=0
        for i in range(len(nums)):
            if Max<nums[i]:
                Max=nums[i]
                indexmax=i+1
        for i in range(len(nums)):
            if Min>nums[i]:
                Min=nums[i]
                indexmin=i+1
        #Both elements removed from back
        
        index=len(nums)
        dif1=1
        dif2=1
        dif1+=index-indexmax
        dif2+=index-indexmin
        f1=max(dif1,dif2)
        
        

        #Both elements removed from front 
        front1=indexmax
        front2=indexmin
        t=max(front1,front2)
        
        #one from front and one from back
        back=1
        back+=index-indexmax
        frontm=indexmin 
        total1=frontm+back
        
        back1=1
        back1+=index-indexmin
        frontmi=indexmax
        total2=back1+frontmi
        f=min(total1,total2)
    
        #min no. of deletion
        overall=min(f1,t,f)
        return overall

