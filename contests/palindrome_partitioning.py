from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # Return the number of partition palindromes.
        return self.recursive(s, 0, [], [])
            
    # Check all the possible partitions
    def recursive(self, string, index, temp , answer):
        if index == len(string):
            answer.append(temp)
            return 
        for cur in range(index, len(string)):
            substr = string[index:cur + 1]
            if self.isPalindrome(substr, 0, len(substr) - 1):
                self.recursive(string, cur + 1, temp + [substr], answer)
        return answer
        
    #Check whether the current string is palindrome or not
    def isPalindrome(self, string, left, right):
        if left >= right:
            return True
        if string[left] != string[right]:
            return False
        return self.isPalindrome(string, left + 1, right - 1)
solution = Solution()
string = input()
result = solution.partition(string)
print(result)
