class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hashmap1={}
        for i in s1:
            hashmap1[i]=hashmap1.get(i,0)+1
        hashmap={}
        i=0
        j=0
        
        while j<len(s2):
           
                

            hashmap[s2[j]] = hashmap.get(s2[j], 0) + 1

            if j - i + 1 == len(s1):

                if hashmap1 == hashmap:
                    return True

                first_key = s2[i]
                hashmap[first_key] -= 1

                if hashmap[first_key] == 0:
                    hashmap.pop(first_key)

                i += 1

            j += 1

           
        return False