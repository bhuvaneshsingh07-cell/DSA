class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=[]
        for ch in s:
            result.append(ord(ch))
        counter=0
        for i in range(len(result)-1):
            counter+=abs(result[i]-result[i+1])
        return counter
        

