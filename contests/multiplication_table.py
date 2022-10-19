def lessthanCurrent(mid, n, m):
    count = 0
    row = 1
    while row <= n:
        count += min(m, mid // row) 
        row +=1
    return count 
def main():
    n, m, k = list(map(int, input().split()))
    left = 1
    right = n * m
    while left <= right:
        mid = (left + right) // 2
        count = lessthanCurrent(mid, n, m) 
        if count < k:
            left = mid + 1
        else:
            right = mid - 1
    return print(left) 
main()
    