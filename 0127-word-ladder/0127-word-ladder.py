class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList + [beginWord]:
            for index in range(len(word)):
                cur_word = word[:index] + "*" + word[index + 1:]
                graph[cur_word].append(word)
        queue = deque([beginWord])
        visited = set([beginWord])
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return level + 1
                for index in range(len(word)):
                    cur_word = word[:index] + "*" + word[index + 1:]
                    for neighbor in graph[cur_word]:
                        if neighbor not in visited:
                            visited.add(word)
                            queue.append(neighbor)
            level += 1
        return 0
