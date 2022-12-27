class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remain = []
        for index in range(len(capacity)):
            remain.append(capacity[index] - rocks[index])
        remain.sort()
        answer = 0
        current = additionalRocks
        for value in remain:
            current -= value
            if current < 0:
                return answer
            answer += 1
            
        return answer
    