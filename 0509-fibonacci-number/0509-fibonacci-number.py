class Solution(object):
    def fib(self,nums):
        if nums==0 or nums==1:
            return nums
        return self.fib(nums-1)+self.fib(nums-2)
