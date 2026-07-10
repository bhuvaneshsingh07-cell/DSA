class Solution(object):
    def maximumWealth(self, accounts):
        self.accounts=accounts
        m=len(accounts)
        n=len(accounts[0])
        
        wealth=0
        for i in range(0,m):
            sum=0
            for j in range(0,n):
                sum+=accounts[i][j]
                
            if sum>wealth:
                wealth=sum
        return wealth

    
        

