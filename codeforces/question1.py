def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    test = get_int()
    for _ in range(test):
        n, c = input().split()
        string = input()
        string += string
        
        cnt = 0
        state = 'a'
        ans = 0
        for char in string:
            if char == c:
                state == c
            elif char == 'g' and state == c:
                ans = max(ans, cnt)
                cnt = 0
                state = 'a'
            elif state == c:
                cnt += 1
        print(ans)
                
            
            
            
            
                
            
             
            #ryrgryy
        

main()