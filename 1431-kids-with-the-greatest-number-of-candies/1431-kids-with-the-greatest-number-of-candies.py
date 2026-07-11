class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        self.candies=candies
        self.extraCandies=extraCandies
        a=[True]*len(candies)
        for i in range(0,len(candies)):
            d=candies[i]+extraCandies
            for j in range(0,len(candies)):
                if d<candies[j]:
                    a[i]=False
        return a
        
        
        

