class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # The idea is simple: If there is a number that is the power of 2 between left and right,
        # The Bitwise AND of all the number will become zero. Because the Bitwise and of the power of 2 and its consecutive number 
        # is zero. Example the bitwise AND of 2**3 = 8 & 7 = 0 and 8 & 9 = 0 
        #Now we can find a number that is the power of 2 between left and right
        #IF exist, just return zero. Because the bitwise AND of zero(due to the two consecutive numbers) and any number is zero
        #Else just do Bitwise AND of those small range numbers.
        #If the range is high, we are sure that we can get a power of 2 between those two ranges and then we will return zero.
        
        index = curNum = 0
        AND = -1 # all bits are on like => 11111....
        while curNum <= left:
            curNum = 2**index  # Exponential expansion => very very fast.
            index += 1
        if curNum < right:
            return 0
        for num in range(left, right + 1):
            AND &= num
        return AND
        
        
        
    

            
        