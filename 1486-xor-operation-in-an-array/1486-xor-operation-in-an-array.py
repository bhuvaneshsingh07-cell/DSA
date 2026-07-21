class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        arr=0
        nums=[0]*n
        for i in range(n):
            nums[i]=start+2*i
        for i in range(n):
            arr=arr^nums[i]
        return arr
            
    