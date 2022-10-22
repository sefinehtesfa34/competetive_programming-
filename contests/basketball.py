
n  = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))
memo = {}
def dp(i, turn):
    # base case
    if (i, turn) in memo:
        return memo[(i,turn)]
        
    if i == len(team2):
        return 0
    if turn == 1:
        memo[(i,turn)] = max(dp(i + 1, turn), team1[i] + dp(i + 1, 2))
        return memo[(i, turn)]
    memo[(i, turn)] = max(dp(i + 1, turn), team2[i] + dp(i + 1, 1))
    return memo[(i, turn)]
def main():
    print(max(dp(0, 1), dp(0, 2)))
    
import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()