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
        if (n == 3 and sum(nums) in nums) or count[0] == n:
            print('YES')
        else:
            print("NO")
main()