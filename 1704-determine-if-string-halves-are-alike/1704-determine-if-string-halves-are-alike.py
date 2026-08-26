class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)//2
        fhalf= s[n:]
       
        shalf=s[:n]
        fvowel=0
        svowel=0
        vowel="aeiouAEIOU"
        
        for i in fhalf:
            if i in vowel:
                fvowel+=1
        for j in shalf:
            if j in vowel:
                svowel+=1
                       
        if fvowel==svowel:
            return True
        else:
            return False       