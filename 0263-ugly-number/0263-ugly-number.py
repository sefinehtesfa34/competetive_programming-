class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def recursive(n):
            if n == 1 or n == -1:
                return True
            if n % 2 == 0:
                return recursive(n // 2)
            if n % 3 == 0:
                return recursive(n // 3)
            if n % 5 == 0:
                return recursive(n // 5)
            return False
        return recursive(n)