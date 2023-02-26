def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n = get_int()
    if n == 0:
        print(1)
    else:
        n %= 8
        if n == 0:
            print(6)
        else:
            value = (1378**n)
            print(int(str(value)[-1]))
    
main()