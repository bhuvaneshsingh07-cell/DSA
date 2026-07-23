class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        #For checking that triangle is poosible
        if nums[0]+nums[1]<=nums[2] or nums[1]+nums[2]<=nums[0] or nums[2]+nums[0]<=nums[1]:
            return "none"
        # for Equilateral
        elif nums[0]==nums[1] and nums[1]==nums[2] and nums[2]==nums[0]:
            return "equilateral"
        #for isoscles
        elif nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]:
            return "isosceles"
        elif nums[0]!=nums[1] and nums[1]!=nums[2] and nums[2]!=nums[0]:
            return "scalene"

