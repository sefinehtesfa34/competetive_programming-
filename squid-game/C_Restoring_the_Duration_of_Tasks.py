def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test  = get_int()
    for _ in range(test):
        n = get_int()
        s =  get_nums()
        f = get_nums()
        ans = 0
        answer = [0]*n 
        for index in range(n):
            ans += f[index] - max(s[index],  f[index - 1] if index > 0 else 0)
            answer[index] = ans 
        print(*answer)
main()