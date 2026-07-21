class Solution(object):
    def threeConsecutiveOdds(self, nums):
       

        
        for i in range(0,len(nums)-2):
            if nums[i]%2!=0 and nums[i+1]%2!=0 and nums[i+2]%2!=0:
               return True
        return False
