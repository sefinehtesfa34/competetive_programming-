class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        count=0
        val=0
        for i in range(len(text)):
            for j in range(len(brokenLetters)):
                if brokenLetters[j] in text[i]:
                    break
                else:
                    count+=1
            if count==len(brokenLetters):
                val+=1
            count=0
        return val
        