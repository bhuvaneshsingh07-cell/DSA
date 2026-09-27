class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(nums)
        i=0
        j=1
        for num in nums:
            if num%2==0:
                ans[i]=num
                i+=2
            else:
                ans[j]=num
                j+=2
        return ans

       