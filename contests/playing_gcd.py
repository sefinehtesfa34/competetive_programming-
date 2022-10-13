def gcd(num1, num2):
    if num2 == 0:
        return num1 
    return gcd(num2, num1 % num2)
def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)
t = int(input())
for _ in range(t):
    n = int(input())
    gcds = list(map(int, input().split()))
    right = 1
    result = "YES"
    while right < len(gcds) - 1:
        lcm1 = lcm(gcds[right - 1], gcds[right])
        lcm2 = lcm(gcds[right], gcds[right + 1])
        curGcd = gcd(lcm1, lcm2)
        if curGcd != gcds[right]:
            result = "NO"
            break
        right += 1
    print(result) 
    