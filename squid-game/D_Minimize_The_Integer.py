from collections import Counter
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        nums = list(input())
        values=  []
        index = 0
        while index < len(nums):
            pos = index 
            while pos > 0 and (int(nums[pos]) % 2 !=  int(nums[pos - 1]) % 2):
                if nums[pos - 1] < nums[pos]:
                    break 
                nums[pos - 1], nums[pos] = nums[pos], nums[pos - 1]
                pos -= 1
            index += 1
        print("".join(map(str, nums)))
        
main()