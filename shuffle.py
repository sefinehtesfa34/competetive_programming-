import random
class Solution:
    def shuffledArrayRecursively(self, cards, index):
        if index == 0:
            return cards 
        cards = self.shuffledArrayRecursively(cards, index - 1)
        randomIndex = self.rand(0, index)
        cards[randomIndex], cards[index] = cards[index], cards[randomIndex]
        return cards 
    def rand(self, lower, higher):
        return lower + int(random.random() * (higher - lower + 1))
solution = Solution()
cards = [1,2,3,4,5]
shuffledCards = solution.shuffledArrayRecursively(cards, len(cards) - 1)
print(shuffledCards)

