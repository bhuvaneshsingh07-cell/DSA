class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        a=len(items)
    
        sum=0
        for i in range(0,a):
           if ruleKey=="type":
            if items[i][0]==ruleValue:
                sum+=1
           if ruleKey=="color":
            if items[i][1]==ruleValue:
                    sum+=1
           if ruleKey=="name":
            if items[i][2]==ruleValue:
                    sum+=1
        return sum           

