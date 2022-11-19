from string import ascii_lowercase, ascii_uppercase
from collections import Counter
def get_int():
    return int(input())
def main():
    n = get_int()
    string = input()
    for lower, upper in zip(ascii_lowercase, ascii_uppercase):
        if lower not in string and upper not in string:
            print("NO")
            break
    else:
        print("YES")
main()
