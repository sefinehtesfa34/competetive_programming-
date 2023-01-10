from cmath import inf


def get_int():
  return int(input())
def get_nums():
  return list(map(int, input().split()))
def main():
    n, k = get_nums()
    nums = get_nums()
    dp = [inf]*n
    dp[0] = 0
    for index in range(n):
        for cur in range(index + 1, k + index + 1):
            if cur < n:
              dp[cur] = min(dp[cur], dp[index] + abs(nums[cur] - nums[index]))
    print(dp[n-1])
          
main()
