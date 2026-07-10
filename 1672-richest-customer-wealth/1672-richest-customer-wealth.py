class Solution(object):
    def maximumWealth(self, accounts):
        self.accounts=accounts
        m=len(accounts)
        n=len(accounts[0])
        arr=[0]*m
        for i in range(0,m):
            sum=0
            for j in range(0,n):
                sum+=accounts[i][j]
                arr[i]=sum
        return max(arr)

    
        

