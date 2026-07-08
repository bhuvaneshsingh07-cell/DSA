class Solution(object):
    def buildArray(self, nums):
        self.nums=nums
        a=len(nums)
        ans=[0]*a
        for i in range(a):
            ans[i]=nums[nums[i]]
           
        return ans