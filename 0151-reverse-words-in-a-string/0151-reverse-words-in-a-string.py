class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        alpha=s.split()
        return " ".join(reversed(alpha))