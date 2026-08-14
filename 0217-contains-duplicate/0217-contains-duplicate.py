class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i, 0) + 1
        val=hashmap.values()
        Max=0
        for i in val:
            if i>Max:
                Max=i
        
        if Max>=2:
            return True
        if Max<=1:
            return False
        