from collections import Counter, defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        hashmap = defaultdict(set)
        counter = Counter()
        answer = []
        for ID, time in logs:
            hashmap[ID].add(time)
        for ID in hashmap:
            counter[len(hashmap[ID])] += 1
        for index in range(1, k+1):
            answer.append(counter[index])
        return answer
solution = Solution()
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
print(solution.findingUsersActiveMinutes(logs, k))