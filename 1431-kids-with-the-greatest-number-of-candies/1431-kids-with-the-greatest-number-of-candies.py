class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        self.candies=candies
        self.extraCandies=extraCandies
        b=len(candies)
        a=[True]*b

        for i in range(0,b):
            d=candies[i]+extraCandies
            for j in range(0,b):
                if d<candies[j]:
                    a[i]=False
                
        return a
        
        
        

