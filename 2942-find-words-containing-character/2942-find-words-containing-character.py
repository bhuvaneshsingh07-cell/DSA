class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        a=[]
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j]==x:
                    a.append(i)
                    break
        return a
