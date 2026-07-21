class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product=1
        for i in nums:
            if i==0:
                product=product*0
            elif i<0:
                product=product*-1
            elif i>0:
                product=product*1
        return product