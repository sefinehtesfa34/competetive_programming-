class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        queue=deque(s)
        
        stack=[]
        string=''
        for i in range(len(queue)):
            element=queue.popleft()
            string+=element
            check=False
            for i in range(len(string)):
                if string[i] in queue:
                    check=True
                if check:
                    break
            if not check:
                stack.append(len(string))
                string=''
        return stack
