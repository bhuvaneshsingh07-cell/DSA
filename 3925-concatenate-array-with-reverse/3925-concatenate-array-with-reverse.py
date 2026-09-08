class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        result=nums[:]
        left=0
        right=n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
           
            
            left+=1
            right-=1
        result=result+nums
        return result


        
        