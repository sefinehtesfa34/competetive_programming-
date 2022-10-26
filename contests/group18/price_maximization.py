def get_test():
    return int(input())
def get_n_k():
    return list(map(int, input().split()))
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_test()
    for _ in range(test):
        n, k = get_n_k()
        nums = get_nums()
        cur_result = 0
        modulos = []
        for num in nums:
            cur_result += num // k
            modulos.append(num % k)
        modulos.sort()
        left = 0
        right = n - 1
        while left < right:
            cur_sum = modulos[right] + modulos[left] 
            if cur_sum >= k:
                cur_result += 1
                left += 1
                right -= 1
            else:
                left += 1
        print(cur_result)
main()
            
                
                
                
            
    