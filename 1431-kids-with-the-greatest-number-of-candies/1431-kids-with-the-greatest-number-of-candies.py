class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        self.candies=candies
        self.extraCandies=extraCandies
        mx=max(candies)
        result=[]
        for i in candies:
            if i+extraCandies>=mx:
                result.append(True)
            else:
                result.append(False)
        return result
        