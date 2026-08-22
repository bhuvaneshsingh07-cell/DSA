class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=n
        Sum=0
        product=1
        while n!=0:
            rem=n%10
            if rem==0:
                pass

            Sum+=rem
            product=product*rem
            n=n//10
        total=Sum+product
        if num % (Sum + product) == 0:
            return True
        else:
            return False
        