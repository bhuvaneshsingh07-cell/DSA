class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence)<26:
            return False  
        hashmap={}      
        if len(sentence)>=26:

            for i in range(len(sentence)):
                hashmap[sentence[i]]=hashmap.get(sentence,0)+1
            d=list(hashmap.values())
            count=0
            if len(d)==26:
                for i in d:
                    if i<=1:
                        count+=1
                if count==26:
                    return True
                else:
                    return False
            else:
                return False
                
        