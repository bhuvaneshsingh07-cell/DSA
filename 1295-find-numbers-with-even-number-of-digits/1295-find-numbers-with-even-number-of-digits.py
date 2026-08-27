class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even=0
        arr=[]
        for num in nums:
            count=0

            while num!=0:
                num=num/10
                count+=1
            arr.append(count)
        for a in arr:
            if a%2==0:
                even+=1
        return even

        
        