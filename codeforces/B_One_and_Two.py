from collections import Counter
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        nums = get_nums()
        prod = 1
        dp = [0]*n 
        for index, num in enumerate(nums):
            prod *= num 
            dp[index] = prod
        for index in range(n):
            if dp[-1] // dp[index] == dp[index]:
                print(index + 1)
                break 
        else:
            print(-1)
main()