class Solution:
    def validUtf8(self, data: List[int]) -> bool:
    
        count = 0
        
        for datum in data:

            if count == 0:
                if bin(datum >> 3) == '0b11110':
                    count = 3
                elif bin(datum >> 4) == '0b1110':
                    count = 2
                elif bin(datum >> 5) == '0b110':
                    count = 1
                elif bin(datum >> 7) != '0b0':
                    return False
            else:
                if bin(datum >> 6) != '0b10':
                    return False
                count -= 1
        

        return count == 0