class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for i in (nums):
            hashmap[i]=hashmap.get(i, 0) + 1
        maxelement=float('-inf')
        maxkey=None
        for key in hashmap:
            if hashmap[key]>maxelement:
                maxelement=hashmap[key]
                maxkey=key
        return maxkey