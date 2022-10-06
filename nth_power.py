from functools import cache
import time 
start = time.time()
class Solution:
    def nthPower(self, n, x):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            return self.nthPower(n//2, x) * self.nthPower(n//2, x)
        return x * self.nthPower(n//2, x) * self.nthPower(n//2, x)
solution= Solution()
n, x = list(map(int, input().split()))
result = solution.nthPower(n, x)
print(result)
end = time.time()
print(end - start)
'''
n = 8
x = 5
   x
  / \
x**4  x** 4
/    \
x**2  x**2 
/   \
x**1 x**1



'''