class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        a=str(num)
       

        count=0
        for i in range(0,len(a)):
            d=num%int(a[i])

            if d==0:

                count+=1
        return count