class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
    
        """
        vowel="aeiouAEIOU"

        i=0
        j=len(s)-1
        while i<=j:
            if s[i] in vowel:
                if s[j] in vowel:
                    s=list(s)
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
                   
                else:
                    j-=1
            else:
                i+=1
        s = ''.join(s)
        return s
        