from math import *
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n = get_int()
        nums = list(input())
        left = 0
        right = n-1
        ans = 'No'
        def is_palindrome(nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] != nums[right]:
                    return False 
                left += 1
                right -= 1
            return True 
        while left < right:
            if nums[left] != nums[right]:
                break 
            left += 1
            right -= 1
        while left < right:
            if nums[right] == nums[left]:
                if is_palindrome(nums[left:right+1]):
                     ans = 'Yes'
                break 
            left += 1
            right -= 1
        if right <= left:
            ans = 'Yes'
        print(ans)
        
        
main()