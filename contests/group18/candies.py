from cmath import inf
from typing import Counter


def main():
    queries = int(input())
    for _ in range(queries):
        n = int(input())
        nums = list(map(int, input().split()))
        count = Counter(nums)
        values = sorted(count.values())
        print(values)
        total = 0
        prev = inf
        counter = 0
        for index in range(len(values) - 1, -1, -1):
            
            if values[index] == prev:
                counter += 1
            total += min(values[index], prev - counter)
            prev = values[index]
        print(total)
main()

        
        