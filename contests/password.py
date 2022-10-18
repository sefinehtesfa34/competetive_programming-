def getDigits():
    return list(map(int, input().split()))
def getNumUnrememberedDigits():
    return int(input())
def main():
    test = int(input())
    for _ in range(test):
        unused = getNumUnrememberedDigits()
        getDigits()
        # The number of combinations to choice r from N  = N!/((N - r)!*r!)
        combinations = (10 - unused) * (10 - unused - 1)//2
        result = 6 * combinations # Total number of choices
        print(result)
main()

