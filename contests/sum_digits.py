temp = list(map(int,input().split()))
m,s = temp[0],temp[1]
high = [0]
def dfs(digits,arr,total):
    if digits == 0:
        if total == s:
            high[0] = max(high[0],int(''.join(arr)))
        return
    if arr and arr[0]=='0':
        return
    for i in range(10):
        dfs(digits-1,arr+[str(i)],total+i)
dfs(m,[],0)
print(high[0])
    