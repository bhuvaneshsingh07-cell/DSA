class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[nums[0]]
        arr2=[nums[1]]
       
        for i in range(2,len(nums),1):
            a=arr1[-1]
            b=arr2[-1]
            if a>b:
                arr1.append(nums[i])
            if b>a:
                arr2.append(nums[i])
        Sum=arr1+arr2
        return Sum

        