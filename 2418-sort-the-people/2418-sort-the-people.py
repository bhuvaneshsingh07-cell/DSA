class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        hashmap={}
        result=[0]*len(names)
       
        n=len(names)
        for i in range(n):
            hashmap[heights[i]]=names[i]
       
        heights.sort(reverse=True)
        
        for i in range(n):
            key=heights[i]
            result[i]=hashmap[key]
        return result
        
        