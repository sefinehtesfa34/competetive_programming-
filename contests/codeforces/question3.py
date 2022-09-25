n = int(input())
nums = list(map(int, input().split()))
product = 1
temp = []
oper = 0
counter = 0
for num in nums:
    if num == 0:
        counter += 1
        continue 
    if num < 0:
        temp.append(-1)
    elif num > 0:
        temp.append(1)
    
    oper += abs(1 - abs(num))
    
for num in temp:
    product *= num 
if product < 0 and counter == 0:
    oper += 2
else:
    oper += counter 
print(oper)
'''
1 0 0 -1
'''