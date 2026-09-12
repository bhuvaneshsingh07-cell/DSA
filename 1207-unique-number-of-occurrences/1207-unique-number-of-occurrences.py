class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashmap={}
        for i in arr:
            hashmap[i]=hashmap.get(i,0)+1
        value=hashmap.values()
        if len(value)==len(set(value)):
            return True
        else:
            return False       