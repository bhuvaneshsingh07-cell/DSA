class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
    
        a=len(nums)
        b=[0]*2
        for i in range(0,a):
            for j in range(1,a):
                if i==j:
                    pass
               
                elif nums[i]+nums[j]==target:
                    b[1]=j
                    b[0]=i
                   
        return b 