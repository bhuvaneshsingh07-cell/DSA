class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(sentences)):
            
            a=sentences[i]
            d=a.split()
            t=len(d)
            if count<t:
                count=t
        return count
        
