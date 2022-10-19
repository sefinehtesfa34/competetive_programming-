def get_length():
    return int(input())
def get_heights():
    return list(map(int, input().split()))
def main():
    n = get_length()
    heights = get_heights()
    minPay = 0 
    total = 0
    prev = 0
    for height in heights:
        total += prev - height 
        if total < 0:
            minPay += abs(total)
            total = 0
        prev = height 
    print(minPay)
main()
    