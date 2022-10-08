class Solution:
    def calculator(self, expression):
        if not expression:
            return 0
        if len(expression) == 1:
            return expression[0]
        stack = []
        operations = ["+","-","*","/"]
        for char in expression:
            if self.isEmpty(stack) or self.isOperation(char, operations):
                stack.append(char)
                continue 
            oper = stack.pop()
            if oper != "*" and oper != "/":
                stack.append(oper)
                continue  
            firstNum = stack.pop()
            value = self.calculate(stack, oper, firstNum, char)
            stack.append(value)
        return self.finalResult(stack)
    
    def finalResult(self, stack):
        if len(stack) == 1:
            return stack[0]
        left = result = 0
        mid = 1
        right = 2
        while right < len(stack):
            result += self.calculate(stack[mid], stack[left], stack[right])
            left += 3
            right += 3
            mid += 3
        return result 
    def isOperation(self, char, operations):
        return char in operations
    def isEmpty(self, stack):
        return len(stack) > 0
    def calculate(self, oper, firstNum, secondNum):
        if oper == "*":
            return int(firstNum) * int(secondNum) 
        if oper == '/':
            return int(firstNum) / int(secondNum) 
        if oper == '+':
            return firstNum + secondNum
        if oper == '-':
            return firstNum - secondNum
solution = Solution()
expression = input()
result = solution.calculator(expression)
print(result)
            
    
    