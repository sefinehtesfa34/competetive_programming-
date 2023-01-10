def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    for _ in range(get_int()):
        n, m, k = get_nums()
        dp = [[0]*(3) for _ in range(n + 1)]
        for index in range(1, n + 1):
            for cur in range(3):
                dp[index][cur] = dp[index - 1][cur]
        
        
        
main()