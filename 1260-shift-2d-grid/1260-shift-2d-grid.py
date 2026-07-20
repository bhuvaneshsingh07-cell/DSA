class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(grid)
        n=len(grid[0])
        ans=[[0 for i in range(n)]for j in range(m)]  
        
        for i in range(m):
            for j in range(n):
                index=i*n+j+k
                newrow=(index/n)%m
                newcol=index%n
                ans[newrow][newcol]=grid[i][j]
        return ans