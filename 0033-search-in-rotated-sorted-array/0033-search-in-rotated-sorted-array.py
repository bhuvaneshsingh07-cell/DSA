class Solution(object):
    def binary(self,i,j,target,arr):
       
        while i<=j:
            mid=(i+j)/2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return -1
        
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivotans=-1
        i=0
        j=len(arr)-1
        while i<=j:
            mid=(i+j)/2
            if arr[mid]<=arr[len(arr)-1]:
                j=mid-1
            else:
                pivotans=mid
                i=mid+1
        if pivotans==-1:
            i=0
            j=len(arr)-1
            result=self.binary(i,j,target, arr)
            return result
        else:
            startarr1=0
            endarr1=pivotans
            if arr[startarr1]<=target and arr[endarr1]>=target:
                result=self.binary(startarr1,endarr1,target,arr)
                return result
               

        
            startarr2=pivotans+1
            endarr2=len(arr)-1
            if arr[startarr2]<=target and arr[endarr2]>=target:
                result=self.binary(startarr2,endarr2,target,arr)
                return result
        return -1       