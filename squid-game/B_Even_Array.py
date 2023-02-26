def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test  = get_int()
    for _ in range(test):
        n = get_int()
        nums =  get_nums()
        even = 0
        odd = 0
        for index in range(n):
            mod1 = index % 2
            mod2 =nums[index] % 2
            if mod1 != mod2:
                if nums[index] % 2:
                    odd += 1
                else:
                    even += 1
        # print(odd, even)
        if even != odd:
            print(-1)
        else:
            print(even)
main()