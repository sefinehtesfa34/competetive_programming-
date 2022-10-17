class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        self.answer = False
        def isInterleave(ptr1, ptr2):
            return ptr1 == len(ptr1) and ptr2 == len(ptr2)

        def dp(ptr1, ptr2, ptr3):
            if (ptr1, ptr2) in memo:
                return memo[(ptr1, ptr2)]
            if ptr3 == len(s3):
                return isInterleave(ptr1, ptr2)
            if ptr1 < len(s1) and s1[ptr1] == s3[ptr3]:
                self.answer = self.answer or dp(ptr1 + 1, ptr2, ptr3 + 1)
            if ptr2 <len(s2) and s2[ptr2] == s3[ptr3]:
                self.answer = self.answer or dp(ptr1, ptr2 + 1, ptr3 + 1)
            memo[(ptr1, ptr2)] = self.answer
            return self.answer
        return dp(0, 0, 0)
      
    
    
    
    
        
        
        