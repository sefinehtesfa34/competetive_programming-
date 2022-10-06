import math
class Solution:
    def generatePrime(self, MAX):
        self.flags = [True for _ in range(MAX + 1)]
        self.flags[0] = False 
        self.flags[1] = False
        prime = 2
        while prime <= math.sqrt(MAX):
            self.crossOff(prime)
            prime = self.nextPrime(prime)
        return self.flags 
            
    def nextPrime(self, prime):
        next = prime  + 1 
        while next < len(self.flags) and not self.flags[next]:
            next += 1
        return next 
    def crossOff(self, prime):
        for index in range(prime * prime, len(self.flags), prime):
            self.flags[index] = False 
    
    
solution = Solution()
MAX = int(input())
flags = solution.generatePrime(MAX)
print(flags)

'''

_______________ takes one hour burn
0  15  30  45  60

_______________ takes one hour to burn
0  15  30 45   60

'''