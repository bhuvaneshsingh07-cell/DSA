class Solution(object):
    def fib(self,nums):
        if nums==0:
            return 0
        elif nums==1:
            return 1
        a,b=0,1
        for i in range(1,nums+2):
            b,a=a,a+b

        return b

