class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = Counter()
        answer = []
        for cur, ingredient in enumerate(ingredients):
            for index in range(len(ingredient)):
                graph[ingredient[index]].append(recipes[cur])
                indegree[recipes[cur]] += 1
        queue = deque(supplies)
        supplies = set(supplies)
        while queue:
            current = queue.popleft()
            if current not in supplies:
                answer.append(current)
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return answer
    
    

        