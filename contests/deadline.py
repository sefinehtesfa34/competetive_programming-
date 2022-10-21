class Solution:
    def max_score(self):
        n = self.get_num()
        tasks = self.get_tasks(n)
        score = 0
        durations = 0
        tasks.sort()
        for task in tasks:
            score += task[1] - (task[0] + durations)
            durations += task[0]
        return print(score)
    
    def get_num(self):
        return int(input())
    
    def get_tasks(self, n):
        tasks = []
        for _ in range(n):
            tasks.append(list(map(int, input().split())))
        return tasks 
solution = Solution()
solution.max_score()
