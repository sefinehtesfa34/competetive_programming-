
# n  = int(input())
# team1 = list(map(int, input().split()))
# team2 = list(map(int, input().split()))
# memo = {}
# def dp(i, turn):
#     # base case
#     if (i, turn) in memo:
#         return memo[(i,turn)]
        
#     if i == len(team2):
#         return 0
#     if turn == 1:
#         memo[(i,turn)] = max(dp(i + 1, turn), team1[i] + dp(i + 1, 2))
#         return memo[(i, turn)]
#     memo[(i, turn)] = max(dp(i + 1, turn), team2[i] + dp(i + 1, 1))
#     return memo[(i, turn)]
# def main():
#     print(max(dp(0, 1), dp(0, 2)))
    
# import sys
# import threading
# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
def get_nums():
    return list(map(int, input().split()))

def main():
    
    n = int(input())
    nums1 = get_nums()
    nums2 = get_nums()
    dp = [[0]*(len(nums1) + 1) for _ in range(2)]
    max_score = 0
    for index in range(1, n + 1):
        
        dp[0][index] = max(dp[0][index - 1], nums1[index - 1] + dp[1][index - 1])
        dp[1][index] = max(dp[1][index - 1], nums2[index - 1] + dp[0][index - 1])
        
        max_score = max(max_score, dp[0][index], dp[1][index])
        
    return print(max_score)
main()


'''

5
9 3 5 7 3
5 8 1 4 5

[[0, 2, 10], 
[0, 1, 3]]


    [                               ]
[0]  
[1]


'''
        
    