class Solution(object):
    def fib(self, n):
        def func(nums):
            if nums==0 or nums==1:
                return nums
            return func(nums-1)+func(nums-2)
        a=func(n)
        return a
