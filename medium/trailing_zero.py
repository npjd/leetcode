from math import log

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        num_fives = 0
        while n > 0:
            num_fives += n//5
            n = n //  5
        return num_fives

