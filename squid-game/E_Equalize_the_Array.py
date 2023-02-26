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
        counter = Counter(nums)
        prefix = [0]*(n + 2)
        for key, value in counter.items():
            prefix[1] += 1
            prefix[value + 1] -= 1
        for index in range(1, n + 2):
            prefix[index] += prefix[index - 1]
        ans = 0
        for index in range(n + 2):
            ans = max(ans, prefix[index]*index)
        print(n-ans)
            
        
        
main()