def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def get_twos(num):
    for index in range(32, 0, -1):
        if num % 2**index == 0:
            return index 
    return 0

def get_min(n, count, nums):
    if count >= n:
        return 0
    nums.sort(reverse = True)
    operations = 0
    for num in nums:
        count += num 
        operations += 1
        if count >= n:
            return operations
    return -1
    
def main():
    test = get_int()
    for _ in range(test):
        n = int(input())
        nums = get_nums()
        count = 0
        for index, num in enumerate(nums):
            twos = get_twos(num)
            count += twos 
            if (index + 1) % 2 == 0:
                nums[index] = get_twos(index + 1)
            else:
                nums[index] = 0
        print(get_min(n, count, nums))
        
main()
    
                
            
    
    
    
    
    
    
    