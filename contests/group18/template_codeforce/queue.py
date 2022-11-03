def get_int():
    return int(input())
def main():
    n = get_int()
    array = [0]*n
    right_hashmap = {} 
    left_hashmap = {}
    nums = set()
    for _ in range(n):
        left, right = list(map(int, input().split()))
        if left == 0:
            array[1] = right 
        if right == 0:
            array[n - 2] = left 
        right_hashmap[left] = right 
        left_hashmap[right] = left
        nums.add(left)
        nums.add(right)
    nums = list(nums)
    start = 0
    end = 0
    for index in range(len(nums)):
        if nums[index] not in left_hashmap:
            start = nums[index]
        if nums[index] not in right_hashmap:
            end = nums[index]
    array[0] = start 
    array[n - 1] = end 
    index = 0
    while index + 2 < n:
        value = array[index]
        if value != 0 and value in right_hashmap:
            array[index + 2] = right_hashmap[value]
        index += 1
    while index - 2 >= 0:
        value = array[index]
        if value != 0 and value in left_hashmap:
            array[index - 2] = left_hashmap[value]
        index -= 1
    print(*array)
main()
        
        
        
        
        
        
        
     
    