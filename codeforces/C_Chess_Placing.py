from collections import Counter
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def main():
    n = get_int()
    nums = get_nums()
    dp = [0]*n 
    for index in range(n):
        if index % 2 == 0:
            dp[index] = 'B'
        else:
            dp[index] = 'W' 
    def compare(char):
        temp = list(dp)
        count = 0
        for num in nums:
            left = -1
            right = -1
            for index in range(n):
                if temp[index] == char:
                    if index < num and temp[index] == char:
                        left = index 
                    elif index >= num and dp[index] == char:
                        right = index 
                        break
            if left ==-1 and right ==-1:
                return float('inf')
            dis1 = dist2 = float('inf')
            if left != -1:
                dis1 = num - left - 1
            if right != -1:
                dis2 = right - num + 1
            if dis1 <= dis2:
                count += dis1 
                temp[left] = '#'
            if dis2 < dis1:
                count += dis2 
                temp[right] = '#'
        return count 
    
    count = min(compare('B'), compare('W'))
    print(count)
    
    
    
            
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
main()