class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        minLength = len(cards) + 1
        counter = Counter()
        for index in range(len(cards)):
            counter[cards[index]] += 1
            while counter[cards[index]] == 2 and left < len(cards):
                minLength = min(minLength, index - left + 1)
                counter[cards[left]] -= 1
                left += 1
        return minLength if minLength != len(cards) + 1 else -1
