class Solution(object):
    def numIdenticalPairs(self, nums):
        
        a=len(nums)
        sum=0
        for i in range(0,a):
            for j in range(0,a):
                if nums[i]==nums[j] and i<j:
                    sum+=1
        return sum
