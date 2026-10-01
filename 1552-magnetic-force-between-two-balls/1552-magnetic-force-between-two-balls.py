class Solution(object):
    def magneticball(self,mid,position,m):
        cowcount=1
        lastposition=0
        for i in range(1,len(position)):
            if position[i]-position[lastposition]>=mid:
                cowcount+=1
                lastposition=i
                if cowcount==m:
                    return True
        return False



    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        n=len(position)
        e=position[n-1]-position[0]
        s=1
        ans=-1
        while s<=e:
            mid=s+(e-s)/2
            if self.magneticball(mid,position,m):
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans
 
        
        