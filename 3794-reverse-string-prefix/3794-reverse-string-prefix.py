class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        

        rev=''
    
        for i in range(k-1,-1,-1):
            rev=rev+s[i]
        rev=rev+s[k:]
        return rev 
