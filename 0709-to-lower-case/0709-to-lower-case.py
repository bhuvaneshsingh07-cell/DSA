class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
          
        b=""          
        for i in s:
            if i.isupper():



                b+=chr(ord(i)+32)
            else:
                b+=i       
        return b

        