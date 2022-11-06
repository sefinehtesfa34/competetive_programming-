class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = [True]*(n)
        count = 0
        primes[0] = primes[1] = False   
        for index in range(2, n):
            if primes[index] == False:
                continue
            for curr in range(index ** index, n, index):
                primes[curr] = False 
        for index in range(len(primes)):
            count += int(primes[index])
        print(primes)
        return count 
                
solution = Solution()
n = int(input())
print(solution.countPrimes(n))
