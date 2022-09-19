'''
To clear all bits from the most significant bit through i (inclusive), we create a mask with a 1 at the ith bit (1 
< < i). Then, we subtract 1 from it, giving us a sequence of 0s followed by i ls. We then AND our number 
with this mask to leave just the last i bits. 
        int clearBitsMSBthroughI(int num, inti) 
        { 
        int mask = (1 << i) - 1; 
        return num & mask; 
    } 
    
'''
num = 29
# 16 8 4 2 1
# 1  1 1 0 1
# 0  1 1 0 1
mask = (1 << 2) - 1
print(num & mask)
