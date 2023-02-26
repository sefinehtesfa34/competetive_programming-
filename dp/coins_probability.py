def get_int():
    return int(input())
def get_nums():
    return list(map(float, input().split()))
def main():
    n = get_int()
    prob = [0] + get_nums()
    
    dp = [[0]*(n + 1) for _ in range(n + 1)]
    ans = 0
    dp[0][0] = 1
    
    for index in range(1, n + 1):
        for head in range(index + 1):
            if head == 0:
                dp[index][head] = dp[index - 1][head]*(1 - prob[index])
            else:
                dp[index][head] = dp[index - 1][head - 1]*prob[index] + dp[index - 1][head]*(1 - prob[index])
    for i in range((n + 1)// 2, n + 1) :
        ans += dp[n][i]
    print(ans)
            
    
    
import threading
import sys 
sys.setrecursionlimit(1 << 27)
main_threading = threading.Thread(target=main)
main_threading.start()
main_threading.join()

    