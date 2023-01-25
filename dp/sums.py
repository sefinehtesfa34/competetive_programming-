# Add some code
def get_nums():
    return list(map(int, input().split()))
def fn(a, b, c, d, e, f, n):
    if n == 0:return a
    if n == 1:return b
    if n == 2:return c
    if n == 3:return d
    if n == 4:return e
    if n == 5:return f
    mod_6 = fn(a, b, c, d, e, f, n%6)
    sum_6 = ((n + 5)//6)*(mod_6 + n)//2 
    mod_5 = fn(a, b, c, d, e, f, n%5)
    sum_5 = ((n + 4)//5)*(mod_5 + n)//2
    mod_4 = fn(a, b, c, d, e, f, n%4)
    sum_4 = ((n + 3)//4)*(mod_4 + n)//2
    mod_3 = fn(a, b, c, d, e, f, n%3)
    sum_3 = ((n + 2)//3)*(mod_3 + n)//2
    mod_2 = fn(a, b, c, d, e, f, n%2)
    sum_2 = ((n + 1)//2)*(mod_2 + n)//2
    mod_1 = fn(a, b, c, d, e, f, n%1)
    sum_1 = ((n)//1)*(mod_1 + n)//2 
    return sum_1 + sum_2 + sum_3 + sum_4 + sum_5 + sum_6


def main():
    test = int(input())
    for _ in range(test):
        a, b, c, d, e, f, n = get_nums()
        ans = fn(a, b, c, d, e, f, n) % 10000007
        print(f"Case {_}:", ans)
        
        
main()