class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(1,n+1):
           
            if i>999:
                count+=1
        return count
        