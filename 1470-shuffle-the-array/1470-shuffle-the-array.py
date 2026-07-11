class Solution(object):
    def shuffle(self, nums, n):
        
    
        b=nums[0:n]
        c=nums[n::]
        d=[]
        for i in range(n):
            d.append(b[i])
            d.append(c[i])
        return d        

    
        
        



        



        



