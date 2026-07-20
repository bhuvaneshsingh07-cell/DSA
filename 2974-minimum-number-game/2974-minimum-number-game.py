class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        arr=[]
        
        while len(nums)!=0:
            alice=min(nums)
            alice0=nums.remove(alice)
            bob=min(nums)
            bob0=nums.remove(bob)
            d=arr.append(bob)
            e=arr.append(alice)
           
        return arr
