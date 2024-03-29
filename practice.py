num = 56
print(num - (num & -num))
print(bin(num))
'''

x & (-x) : Returns the rightmost 1 in binary representation of x

(-x) is the two’s complement of x. (-x) will be equal to one’s complement of x plus 1.
Therefore (-x) will have all the bits flipped that are on the left of the rightmost 1 in x. So x & (-x) will return rightmost 1.

x = 10 = (1010)2
(-x) = -10 = (0110)2
x & (-x) = (1010)2 & (0110)2 = (0010)2

3) x | (1 << n) : Returns the number x with the nth bit set.

(1 << n) will return a number with only nth bit set. So if we OR it with x it will set the nth bit of x.
x = 10 = (1010)2 n = 2
1 << n = (0100)2
x | (1 << n) = (1010)2 | (0100)2 = (1110)2 
'''