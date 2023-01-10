def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n = get_int()
    dp =[0,0,0]
    for _ in range(n):
        nums = get_nums()
        new_dp = [0,0,0]
        for index in range(3):
            for cur in range(3):
                if cur != index:
                    new_dp[index] = max(new_dp[index], dp[cur] + nums[index])
        dp = new_dp
    print(max(dp))
main()