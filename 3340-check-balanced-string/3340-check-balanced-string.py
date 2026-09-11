class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        evensum=0
        oddsum=0
        for i in range(0,len(num)):
            if i%2==0:
                evensum+=int(num[i])
            else:
                oddsum+=int(num[i])
        if oddsum==evensum:
            return True
        else:
            return False

