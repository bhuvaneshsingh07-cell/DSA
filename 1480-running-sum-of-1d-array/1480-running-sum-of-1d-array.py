class Solution(object):
    def runningSum(self, nums):
        self.nums=nums
        a=len(nums)
        sum=[0]*a
        s=str(nums)
        sum[0]=nums[0]
        ans=sum[0]
        for i in range(1,a):
            ans+=nums[i]
            sum[i]=ans
        return sum