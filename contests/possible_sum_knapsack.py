class Solution:
    def possible_sum(self):
        weights= self.get_weights()
        W = sum(weights)
        possible = [False] * (W+ 1)
        possible[0] = True 
        for index in range(len(weights)):
            for weight in range(W, -1, -1):
                if possible[weight]:
                    possible[weight + weights[index]] = True 
        return print(possible)
    
    def get_weights(self):
        return list(map(int, input().split()))
solution = Solution()
solution.possible_sum()
