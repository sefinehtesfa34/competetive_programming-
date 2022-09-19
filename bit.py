'''
nums = [8 3 7 12 34 67]
    64 32 16 8 4 2 1
34  0  1  0  0 1 0 0  0 1 0 0 1 0 0
67  1  0  0  0 0 1 1  1 1 0 0 1 1 1 
12  0  0  0  1 1 0 0  1 1 0 1 0 1 1
8   0  0  0  1 0 0 0  1 1 0 0 0 1 1 
7   0  0  0  0 1 1 1  1 1 0 0 1 0 0
3   0  0  0  0 0 1 1  1 1 0 0 1 1 1
xor 1  1  0  0 1 1 1  
 

1 1 0 0 1 1 1 
1 1 0 0 1 1 1

'''

xor = 0
nums = [1, 59, 60, 20, 5, 302, 268, 2201, 3061, 3032, 3064, 3003, 2947, 3041]
prefix = []
for num in nums:
    xor^=num 
    prefix.append(xor)
start = 3
end = 7
val = 0
for index in range(start,end):
    val ^= nums[index]
print(val)
print(prefix[end - 1] ^ prefix[start] ^ nums[start])
print(prefix)