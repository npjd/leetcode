class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        counts = [0] * 26
        lookups = [0] * 26
        for i in range(len(s1)):
            counts[ord(s2[i]) - ord('a')] += 1
            lookups[ord(s1[i]) - ord('a')] += 1
        

        for i in range(len(s1), len(s2)):
            print(i)
            if counts == lookups:
                return True
            counts[ord(s2[i-len(s1)]) - ord('a')] -= 1
            counts[ord(s2[i]) - ord('a')] += 1
        if counts == lookups:
            return True

        return False

        
