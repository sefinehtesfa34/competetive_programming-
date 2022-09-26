class Solution:
    def __init__(self, K):
        self.array = [0 ]*(K + 1) 
        
    def rangeAddition(self, startIndex, endIndex, increamental):
        self.array[startIndex]+= increamental
        self.array[endIndex + 1] -= increamental
    def finalArray(self):
        for index in range(1, len(self.array)):
            self.array[index] += self.array[index - 1]
        return self.array[:-1]
K = int(input())
solution = Solution(K)
for _ in range(10):
    startIndex, endIndex, increamental = list(map(int, input().split()))
    solution.rangeAddition(startIndex, endIndex, K)
print(solution.finalArray())

        
        