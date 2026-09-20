class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        for i in range(len(s)):
            value = 26 - (ord(s[i]) - ord('a'))
            result+=value*(i+1)
        return result
