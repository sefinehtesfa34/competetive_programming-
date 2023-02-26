from collections import *
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n, m = get_nums()
    graph = list()
    for _ in range(n):
        graph.append(input())
    dp = [[0]*(m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if graph[row - 1][col - 1] == '.':
                dp[row][col]  += dp[row - 1][col] + dp[row][col - 1]
    print(dp[n][m] % 1000_000_007)
import threading
import sys 
sys.setrecursionlimit(1 << 27)
main_threading = threading.Thread(target=main)
main_threading.start()
main_threading.join()
