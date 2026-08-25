class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        key=[]
        hashmap={}
        for i in nums1:
            if i in nums2:
                hashmap[i]=hashmap.get(i,0)+1
        for k in hashmap:
            key.append(k)
        return key

        