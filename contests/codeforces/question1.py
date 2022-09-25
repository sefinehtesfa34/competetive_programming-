# t = int(input())
# while t:
#     # n,k = list(map(int, input().split()))
#     n = int(input())
#     nums= set(map(int, input().split()))
#     if len(nums) <= 2:
#         print(0)
#     else:
#         print(len(nums) - 2)
    
    
#     t-=1 
from typing import Counter


n = int(input())
nums= list (map(int, input().split()))

counter = Counter(nums)
setVal = set(nums)
listVal = sorted(setVal)
result = 0
for index in range(1, len(listVal) -1):
    result += counter[listVal[index]]
print(result)
