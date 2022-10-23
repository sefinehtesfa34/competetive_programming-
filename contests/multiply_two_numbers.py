class Solution:
    def multiply_two_numbers(self):
        num1, num2 = self.get_nums()
        smaller = num1 if num1 < num2 else num2 
        bigger = num1 if num1 > num2 else num2 
        return self.recursive(smaller, bigger)
     
    def recursive(self, smaller, bigger):
        if smaller == 0:
            return 0
        if smaller == 1:
            return bigger
        half  = self.recursive(smaller//2, bigger)
        if smaller % 2 != 0:
            return half + half + bigger 
        return half + half 
    
    def get_nums(self):
        return list(map(int, input().split()))
solution = Solution()
product = solution.multiply_two_numbers()
print(product)