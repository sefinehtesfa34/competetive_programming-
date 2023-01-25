test = int(input())
for _ in range(test):
    n, k = list(map(int, input().split()))
    dp = [[0]*(k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for index in range(n + 1):
        dp[index][1] = 1
    for row in range(n + 1):
        for col in range(k + 1):
            dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]
    comb = dp[n][k]
    print(comb)