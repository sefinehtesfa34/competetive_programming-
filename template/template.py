from heapq import * 
from collections import *
from math import *
from itertools import accumulate
from string import ascii_lowercase,ascii_uppercase
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def get_str():
    return input()
def main():
    test = get_int()
    for _ in range(test):
        n, k = get_nums()
        nums = get_nums()
        nums.sort(reverse= True)
        x = 0
        answer = 0
        for index in range(n):
            if nums[index] % k == 0:
                continue 
            answer += k - ((nums[index] + x) % k) 
            x += k - ((nums[index] + x) % k) 
        print(answer)
        
main()    

'''


    scanf("%s",s+1);
    int len = strlen(s+1);
    for(int i=1;i<=len;i++)
    {
        low[i]=low[i-1];
        high[i]=high[i-1];
        if(s[i]<='z'&&s[i]>='a')
            low[i]++;
        else
            high[i]++;
    }
    int ans = 9999999;
    for(int i=0;i<=len;i++)
    {
        ans = min(ans,i-high[i]+(high[len]-high[i]));
    }
    printf("%d\n",ans);
'''