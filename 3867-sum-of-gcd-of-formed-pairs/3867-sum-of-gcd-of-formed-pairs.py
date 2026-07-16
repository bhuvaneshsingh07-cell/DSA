class Solution(object):
    def gcdSum(self, nums):
        a=len(nums)
        prefixgcd=[0]*a
        def GCD(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        Max=nums[0]

        for i in range(0,a):
            if Max<nums[i]:
                Max=nums[i]
        
            prefixgcd[i]=GCD(nums[i],Max)
        prefixgcd.sort()
        left=0
        right=a-1
        s=0
        while left<right:
            s+=GCD(prefixgcd[left],prefixgcd[right])
            

            left+=1
            right-=1
        return s

