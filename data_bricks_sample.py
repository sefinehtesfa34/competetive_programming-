def solution(s):
    def checker(left, right):
        while left < right:
            if s[left] != s[right]:
                return False 
            left += 1
            right -= 1
        return True
    def dfs(left, right):
        if left == right:
            return s[left]
        if left > right:
            return ''
        
        for index in range(right, left, -1):
            is_palindrome = checker(left, index)
            if is_palindrome:
                return dfs(index + 1, right)
        return s[left:right + 1]
    result = dfs(0, len(s) - 1)
    return result if result else ""
result = solution("aaacodedoc")
print(result)