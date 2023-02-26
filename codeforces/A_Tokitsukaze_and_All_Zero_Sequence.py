from collections import Counter
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        nums = get_nums()
        count = Counter(nums)
        zeros = count[0]
        remain = n - zeros
        if zeros > 0:
            print(remain)
        elif len(count) == n:
            print(n + 1)
        else:
            print(n)
main()