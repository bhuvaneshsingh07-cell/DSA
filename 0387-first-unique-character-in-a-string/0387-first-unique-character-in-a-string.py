class Solution(object):
    def firstUniqChar(self, s):
        hashmap={}
        for i in s:
            hashmap[i]=hashmap.get(i,0)+1
        for i in range(0,len(s)):
            value=hashmap.get(s[i])
            if value==1:
                return i
        return -1
