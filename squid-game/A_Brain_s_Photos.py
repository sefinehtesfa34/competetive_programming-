def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n, m = get_nums()
    values = set()
    for _ in range(n):
        cur = input().split()
        for char in cur:
            values.add(char)
    if 'C' in values or 'M' in values or 'Y' in values:
        print('#Color')

    else:
        print("#Black&White")    
main()