class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        str1=""
    
        for i in range(0,len(s)):
            if len(str1)>0 and str1[len(str1)-1]==s[i]:
                str1=str1[:-1]
            
                
            else:

                str1+=s[i]
            
        return str1