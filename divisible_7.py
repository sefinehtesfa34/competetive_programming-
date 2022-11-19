from math import inf
from string import ascii_lowercase, ascii_uppercase
from collections import Counter
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        remain = n % 7 
        if n - remain < 10:
            print(14)
        else:
            print(n - remain)
        
        
        
        
        
        
        
        
        
main()