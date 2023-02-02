class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        words = []
        for word in logs:
            if not word[-1].isalpha():
                digits.append(word)
            else:
                word = word.split()
                words.append((word[1:], word[0]))
        words.sort()
        words = [" ".join([idn] + word) for word, idn in words]
        return words + digits
        
        