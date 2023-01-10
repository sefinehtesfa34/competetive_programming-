from cmath import inf
from collections import Counter, defaultdict


def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n,W = get_int()
    given = []
    for _ in range(n):
        w, v = get_nums()
        given.append([w, v])
    
        
main()