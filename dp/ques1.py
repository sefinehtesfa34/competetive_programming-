from cmath import inf


def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n = get_int()
    dp = [[0]*3 for _ in range(n + 1)]
    nums = []
    for _ in range(n):
        nums.append(get_nums())
        
    for index in range(1, n + 1):
        for cur in range(3):
            for begin in range(3):
                if begin != cur:
                    dp[index][cur] = max(dp[index][cur], nums[index - 1][cur] + dp[index - 1][begin])
    print(max(dp[n]))
    
main()