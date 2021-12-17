class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=["+","-","*","/"]
        stack=[]
        for i in range(len(tokens)):
            if not tokens[i] in l:
                stack.append(tokens[i])
            elif tokens[i]=="*":
                val1=int(stack.pop())
                val2=int(stack.pop())
                stack.append((val1*val2))
            elif tokens[i]=="/":
                val1=int(stack.pop())
                val2=int(stack.pop())
                if abs(val2)<abs(val1):
                    stack.append(0)
                elif val2<0 and val1>0:
                    stack.append(-1*(abs(val2)//val1))
                elif val2>0 and val1<0:
                    stack.append(-1*(val2//abs(val1)))
                else:
                    stack.append((val2//val1))
            elif tokens[i]=="+":
                val1=int(stack.pop())
                val2=int(stack.pop())
                stack.append((val1+val2))
            elif tokens[i]=="-":
                val1=int(stack.pop())
                val2=int(stack.pop())
                stack.append((val2-val1))
        return str(stack[0])