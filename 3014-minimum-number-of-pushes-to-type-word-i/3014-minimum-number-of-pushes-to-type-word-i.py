class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        return sum(i//8+1 for i in range(len(word)))
        
        