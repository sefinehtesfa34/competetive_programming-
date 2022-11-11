from string import *
from heapq import *
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def negative(num):
    return -num 
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        string = input()
        hashmap = {}
        answer = []
        left = 0
        for char in string:
            if char in hashmap:
                answer.append(hashmap[char])
            else:
                if char == ascii_lowercase[left]:
                    left += 1
                if left > 26:
                    left = chr(ord(char) + 1)
                hashmap[char] = ascii_lowercase[left]
                answer.append(hashmap[char])
                left += 1
            left %= 26
        print("".join(answer))
                                    
            # c o d e f o r c e s
            # a b c d e b f a d g
main()

        