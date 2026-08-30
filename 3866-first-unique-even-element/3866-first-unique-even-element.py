class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for i in range(len(nums)):
            value=hashmap.get(nums[i])
            if value==1:
                if nums[i]%2==0:
                    return nums[i]
        return -1