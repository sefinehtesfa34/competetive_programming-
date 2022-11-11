class Solution:
    def minimum_distance(self):
        blue = self.get_nums()
        red = self.get_nums()
        blueCost = self.get_cost()
        dp =[[0]*(len(blue) + 1) for _ in range(2)]
        dp[0][0] = blueCost
        result = 1000000
        answer = []
        for index in range(1, len(blue) + 1):
            dp[0][index] = blue[index - 1] + min(dp[0][index - 1], blueCost + dp[1][index - 1])
            dp[1][index] = red[index - 1] + min(dp[0][index - 1], dp[1][index - 1])
            result = min(dp[0][index], dp[1][index])
            answer.append(result)
        return print(*answer)
    
    def get_nums(self):
        return list(map(int, input().split()))
    
    def get_cost(self):
        return int(input())
solution = Solution()
solution.minimum_distance()
'''
blue = [2,3,4,5]
red = [1,5,2,3]
blueCost = 2

'''