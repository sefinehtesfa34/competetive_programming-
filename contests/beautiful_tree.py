t = int(input())
class Solution:
    def __init__(self):
        self.operations = 0
    def findOperations(self, array):
        if len(array) == 1:
            return array
        mid = (len(array)) //2
        left = self.findOperations(array[:mid])
        right = self.findOperations(array[mid:])
        if left[0] > right[0]:
            self.operations += 1
            return right + left 
        return left + right 
solution = Solution()
for _ in range(t):
    m = int(input())
    permutations = list(map(int, input().split()))
    resultPermutations = solution.findOperations(permutations)
    left = 0
    right = 1
    while right < len(resultPermutations):
        if resultPermutations[right] - resultPermutations[left] != 1:
            print(-1)
            break 
        left += 1
        right += 1
    else:
        print(solution.operations)
    solution.operations = 0