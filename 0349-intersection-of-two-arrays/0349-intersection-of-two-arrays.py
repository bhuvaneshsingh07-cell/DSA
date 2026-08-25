class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=[]
        hashmap={}
        for i in nums1:
            if i in nums2:
                hashmap[i]=hashmap.get(i,0)+1
        for key in hashmap:
            a.append(key)
        return a

        