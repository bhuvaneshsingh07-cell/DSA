class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementsum=0
        digitsum=0
        for i in range(len(nums)):
            elementsum+=nums[i]
        for i in range(len(nums)):
            if nums[i]//10!=0:
                temp=nums[i]

                while temp!=0:
                    digitsum+=temp%10
                    temp=temp//10
            if nums[i]//10==0:
                digitsum+=nums[i]

          
        return elementsum-digitsum