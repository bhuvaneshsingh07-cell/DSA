class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a=len(strs)
        prefix=strs[0]
        
        for i in range (1,a):
            while(strs[i].find(prefix)!=0):
                prefix=prefix[:-1]
        return prefix    