class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n > 0:
            operation = (lambda x: lambda y: x*y)
        else:
            operation = (lambda x: lambda y: x/y)
            n *= -1
        while n > 0:
            if n % 2 == 1:
                res = operation(res)(x)
            x = x*x
            n = n // 2

        return res