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
            divisor = 10 ** (len(str(count)) - 1)

        
            if count>1:
                
                while divisor> 0:
                    digit = count//divisor
                    chars[writeindex]=str(digit)
                    writeindex+=1
                    count = count % divisor
                    divisor //= 10
            

                
        return writeindex
