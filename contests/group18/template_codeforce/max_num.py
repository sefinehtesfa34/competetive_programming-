left, right = list(map(int, input().split()))
def main():
    if left == right:
        return print(0)
    result = 0
    bit_pos = 0
    max_num = max(left, right)
    min_num = min(left, right)
    
    for shift in range(32):
        if max_num & 1<< shift:
            bit_pos = shift
    shift = bit_pos
    while shift >= 0:
        if (max_num & 1 << shift) ^ (min_num & 1 << shift):
            result |= 1 << shift
        elif max_num & 1 << shift and min_num & 1 << shift:
            cur_max = max_num & ~(1 << shift)
            cur_min = min_num & ~(1 << shift)
            if cur_max >= min_num:
                result |= 1 << shift
                max_num = cur_max
            elif cur_min <= max_num:
                result |= 1 << shift
                min_num = cur_min
        else:
            cur_min = min_num | 1 << shift
            if cur_min <= max_num:
                min_num = cur_min
                result |= 1 << shift
        shift -= 1
    
    return print(result)
    
    
    
main()
    