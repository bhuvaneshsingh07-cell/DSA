class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=str(n)
        product=1
        Sum=0
        for i in a:
            product=product*int(i)
            Sum+=int(i)
        return product-Sum