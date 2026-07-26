class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        a=(num)**0.5
        c=int(a)
        d=c*c
        if d==num:
            return True
        else:
            return False        
       