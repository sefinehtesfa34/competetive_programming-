from math import *
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        nums = get_nums()
        dp = [1]*(n + 1)
        for index in range(n):
            for left in range(index):
                if nums[left]^index < nums[index]^left:  
                    dp[index] = max(dp[index], 1 + dp[left])
        print(max(dp)) 
             
main()