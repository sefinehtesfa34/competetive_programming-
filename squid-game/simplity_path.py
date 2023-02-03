class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split('/')
        move = 0
        answer = []
        for folder in folders[::-1]:
            invalid = folder == '/' or folder == '' or folder == '.'
            if folder == '..':
                move += 1
            elif move > 0 and not invalid:
                move -= 1
            elif move == 0 and not invalid:
                answer.append(folder)
        result = '/'.join(answer[::-1])
        return '/' + result
    
    