def get_length():
    return list(map(int, input().split()))
def get_nums():
    return list(map(int, input().split()))
def main():
    n, k = get_length()
    nums = get_nums()
    nums.sort()
    prev = nums[0]
    count = 1
    total_sum = left = 0
    resultNum = nums[0]
    resultCount = 1
    for index in range(1, len(nums)):
        total_sum += (nums[index] - prev) * count 
        while total_sum > k:
            total_sum -= (nums[index] - nums[left]) 
            left += 1
            count -= 1
        count += 1
        if index - left + 1 > resultCount:
            resultCount = index - left + 1
            resultNum = nums[index]
        prev = nums[index]
    print(resultCount, resultNum)
main()



    
    
    
    