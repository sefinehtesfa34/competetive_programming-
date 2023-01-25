def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n, amount = get_nums()
    coins = get_nums()
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    for curr in range(1, amount + 1):
        for coin in coins:
            if coin <= curr:
                dp[curr] += dp[curr - coin]
    return print(dp[amount] % 1000_000_007)
    

main()