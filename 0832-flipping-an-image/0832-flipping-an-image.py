class Solution(object):
    def flipAndInvertImage(self, image):
        
        for i in range(0,len(image)):
        
            image[i]=image[i][::-1]
            for j in range(0,len(image[0])):
               
                if image[i][j]==1:
                    image[i][j]=0
                elif image[i][j]==0:
                    image[i][j]=1                
        return image
        
            
                



