class Solution(object):
    def findGCD(self, nums):
        d=min(nums)
        e=max(nums)
        def gcd(a,b):
            while b!=0:
                a,b= b,a % b
            return a
        
        f=gcd(d,e)
        return f

        