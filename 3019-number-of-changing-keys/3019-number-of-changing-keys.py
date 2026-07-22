class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)-1):
           
            if s[i]==s[i+1] or s[i]==s[i+1].upper() or s[i]==s[i+1].lower() :
                pass
            elif s[i]!=s[i+1] or s[i]!=s[i+1].upper() or s[i]!=s[i+1].lower() :
                count+=1
        return count

