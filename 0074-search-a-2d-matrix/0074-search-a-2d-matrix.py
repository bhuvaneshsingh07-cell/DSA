class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        totalrow=len(matrix)
        totalcol=len(matrix[0])
        totalelement=totalrow*totalcol
        e=totalelement-1
        s=0
        while s<=e:
            mid=s+(e-s)/2
            rowindex=mid/totalcol
            colindex=mid%totalcol
            if matrix[rowindex][colindex]==target:
                return True
            elif matrix[rowindex][colindex]<target:
                s=mid+1
            else:
                e=mid-1
        return False