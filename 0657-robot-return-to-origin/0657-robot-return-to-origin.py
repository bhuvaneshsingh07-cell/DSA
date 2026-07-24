class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l=0
        u=0
        d=0
        r=0
        for i in range(len(moves)):
            if moves[i]=="L":
                l+=1
            elif moves[i]=="R":
                r+=1
            elif moves[i]=="U":
                u+=1
            elif moves[i]=="D":
                d+=1
        if l==r and u==d:
            return True
        else :
            return False