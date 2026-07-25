class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        while n!=0:
            d=n%10
            a.append(d)
            n=n//10
        a.sort(reverse=True)

        Max=1
        Max=a[0]*a[1]
        return Max