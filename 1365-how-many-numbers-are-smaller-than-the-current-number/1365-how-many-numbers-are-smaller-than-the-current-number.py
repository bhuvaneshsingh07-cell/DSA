class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        self.nums=nums
        a=len(nums)
        arr=[0]*a
        for i in range(0,a):
            sum=0
            for j in nums:
                if nums[i]>j:
                    sum+=1
                    arr[i]=sum

                
        return arr