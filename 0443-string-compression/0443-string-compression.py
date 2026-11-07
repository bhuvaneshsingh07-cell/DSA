class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index=0
        writeindex=0
        while index<len(chars):
            current=chars[index]
            count=0

            while index<len(chars) and chars[index]==current:
                index+=1
                count+=1
            chars[writeindex]=current
            writeindex+=1
           
        
            if count>1:
                for i in str(count):
                    chars[writeindex]=i
                    writeindex+=1

                
        return writeindex
