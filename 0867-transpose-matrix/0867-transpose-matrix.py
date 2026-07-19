class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(matrix)
        n=len(matrix[0])
    
        transpose=[[0 for i in range(m)]for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                transpose[i][j]=matrix[j][i]
        return transpose
