class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        output=''
        for i in range(len(s)):
            if s[i]==")":
                index1=i
                for j in range(len(stack)-1,-1,-1):
                    if stack[j]=="(":
                        index2=j
                        stack[index2:index1]=stack[index2+1:index1][::-1]
                        break
            else:
                stack.append(s[i])
        for i in stack:
            output+=i
        return output