class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fhalf=""
        shalf=""
        fvowel=0
        svowel=0
        vowel="aeiouAEIOU"
        for i in range(0,len(s)/2):
            fhalf+=s[i]
        for i in range(len(s)/2,len(s)):
            shalf+=s[i]
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