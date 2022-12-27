class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remain = []
        for index in range(len(capacity)):
            remain.append(capacity[index] - rocks[index])
        remain.sort()
        answer = 0
        current = additionalRocks
        for value in remain:
            if value == 0:
                answer += 1
            elif current >= value:
                current -= value
                answer += 1
            else:
                break
        return answer
    