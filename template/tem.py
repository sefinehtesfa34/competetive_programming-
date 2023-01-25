from math import floor

bit = 0 
x = 20
while x > 0:
    x &= ~(1 << bit) 
    bit += 1
leftmost = max(0, bit - 1)
print(leftmost)