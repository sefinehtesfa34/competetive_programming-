class MinStack:
    
    def __init__(self):
        self.l=[]

    def push(self, val: int) -> None:
        self.l.append(val)

    def pop(self) -> None:
        val=self.l.pop()        
        return val
    def top(self) -> int:
        val=self.l[-1]
        return val

    def getMin(self) -> int:
        val=min(self.l)
        return val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()