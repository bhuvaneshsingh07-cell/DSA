class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
    
        a=len(nums)
        b=[0,0]
        for i in range(0,a-1):
            for j in range(i+1,a):
                if nums[i]+nums[j]==target:
                    b[0]=i
                    b[1]=j
                    return b 