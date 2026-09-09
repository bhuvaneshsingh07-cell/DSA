class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index=0
        count=0
        for i in range(len(word)):
            if ch==word[i]:
                index=i
                count+=1
                break
        if count==0:
            return word
           
        rev=''
        for i in range(index,-1,-1):
            rev=rev+word[i]
        rev=rev+word[index+1:]
        return rev
        