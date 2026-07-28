class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        for i in range(n):
            ans.append((i+1))
        
        for a in range(len(ans)):
            if ans[a]%3==0 and ans[a]%5==0:
                ans[a]="FizzBuzz"
            elif ans[a]%3==0:
                ans[a]="Fizz"
            elif ans[a]%5==0:
                ans[a]="Buzz"
           
        for i in range(len(ans)):
            ans[i]=str(ans[i])
        return ans
        

        