class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        excepted=heights[:]
        for i in range(n-1):
            for j in range(n-1-i):
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
        index=0
        for i in range(n):
            if heights[i]!=excepted[i]:
                index+=1
        return index
                
