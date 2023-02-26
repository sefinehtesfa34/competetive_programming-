from math import *
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        nums = sorted(get_nums())
        ans = 'Yes'
        num1 = num2 = 0
        prev  = float('inf')
        for index in range(n):
            for cur in range(index + 1, n):
                gcd_val = gcd(nums[index], nums[cur])
                if gcd_val < prev:
                    prev = gcd_val
                    num1 = nums[index]
                    num2 = nums[cur]
        nums.remove(num1)
        nums.remove(num2)
        nums = [num1, num2] + nums 
        gcd_val = nums[0]
        for index in range(1, n):
            gcd_val = gcd(nums[index], gcd_val)
            if gcd_val > index + 1:
                ans  = 'No'
        print(ans)
        
        
main()