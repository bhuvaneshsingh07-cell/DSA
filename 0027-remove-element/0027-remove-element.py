class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
       
        n=len(nums)-1
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]

                j-=1
            else:
                i+=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums.remove(val)
        return len(nums)

