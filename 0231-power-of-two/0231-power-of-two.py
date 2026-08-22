class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            return False
        if n==1:
            return True
        value=1
        num=n
        if n%2==0:
           
            while n!=0:
                a=n/2
                value+=a
                n=n/2
            

            if value==num:
                return True
            elif value!=num:
                return False
        else:
            return False
        