class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = left = right = cur_sum = 0
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        for index in range(n - k):
            cur_sum += cardPoints[index]
        index = n - k
        max_score = total_sum - cur_sum
        while index < n:
            cur_sum -= cardPoints[left]
            cur_sum += cardPoints[index]
            max_score = max(max_score, total_sum - cur_sum)
            index += 1
            left += 1
        return max_score