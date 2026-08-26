class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        counter=word1[0]
        counter2=word2[0]
        for alpha in range(1,len(word1)):
            counter+=word1[alpha]
        for beta in range(1,len(word2)):
            counter2+=word2[beta]
        if counter==counter2:
            return True
        else:
            return False