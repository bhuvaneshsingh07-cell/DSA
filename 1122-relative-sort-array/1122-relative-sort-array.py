class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        num=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    num.append(i)
        Max=[]
        for i in arr1:

            if i not in arr2:
                Max.append(i)   
        Max.sort()
        for j in Max:
            num.append(j)
        return num
        