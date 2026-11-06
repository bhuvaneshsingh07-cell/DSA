class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while(part in s):
            index=s.index(part)
        
            s=s[0:index]+s[index+len(part):len(s)+1]        
        return s