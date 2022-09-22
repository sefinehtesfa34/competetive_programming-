t = int(input())
for _ in range(t):
    n,x,y  = list(map(int, input().split()))
    arr = []
    for index in range(1, n):
        total = (n - 1 - index) * x + index * y 
        if total == n - 1:
            arr = [1] * (n - 1 - index) + [n - 1] * index 
            break 
    if not arr:
        print(-1)
    else:
        for winner in arr:
            print(winner, end = " ")
        print()
    
    