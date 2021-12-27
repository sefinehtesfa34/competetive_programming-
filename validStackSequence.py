class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l=[]
        popped=popped[::-1]
        for i in range(len(pushed)):
            if l:                                                             #pushed=[1,2,3,4,5]
                if l[-1]!=popped[-1]:       #l=[1,2,3,5]   #popped=[1,2,3,5]
                    l.append(pushed[i])
                else: 
                    while l[-1]==popped[-1]:
                        l.pop()                                     #popped=[0]
                        popped.pop()
                        if not l:
                            break  
                    l.append(pushed[i])                              #l=[0]
            else:
                l.append(pushed[i])
        if len(l)==len(popped) and l==popped:
            return True
        return False
        
                
                