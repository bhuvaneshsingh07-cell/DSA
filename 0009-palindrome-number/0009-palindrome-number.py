class Solution(object):
    def isPalindrome(self, x):
        self.x=x
        rem=0
        nums=x
        s=str(nums)

        while nums>0:
            rem=(rem*10)+(nums%10)
            nums=nums//10

        if rem==x:
            return True
        elif rem!=x:
            return False
       