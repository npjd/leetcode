class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        ans = set()

        i = 1
        j = 1

        while i < bound:
            while i + j <= bound:
                ans.add(i+j)
                j *= y
                if y == 1:
                    break
            if x == 1:
                break
            i *= x
            j = 1

        return list(ans)