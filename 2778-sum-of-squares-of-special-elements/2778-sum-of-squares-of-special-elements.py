class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumofsq=0
        n=len(nums)
        nums.insert(0,0)
        
        for i in range(1,n+1):
            if n%(i)==0:
            
                sumofsq+=nums[i]*nums[i]
            
        return sumofsq
        