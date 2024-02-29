class Solution:
    def numTrees(self, n: int) -> int:
        numTrees = [1] * (n+1)
    
        for i in range(1, n+1):
            total = 0
            for j in range(0, i):
                total += numTrees[j]*numTrees[i-j-1]
            numTrees[i] = total
        return numTrees[n]