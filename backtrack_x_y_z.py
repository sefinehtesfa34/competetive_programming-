class Solution:
    def find_paths(self):
        string = ['x', 'y','z']
        paths = []
        chosen = {char:False for char in string}
        
        def dfs(path, chosen):
             
            if len(path) == len(string):
                paths.append(list(path))
                return 
            
            for index in range(len(string)):
                 char = string[index]
                 if char  == "z" and chosen['x']:
                     continue 
                 if not chosen[char]:
                    chosen[char] = True 
                    dfs(path + [char], chosen)
                    chosen[char] = False 
                 
        dfs([], chosen)
        return print(paths)
solution = Solution()
solution.find_paths()

            
            
        