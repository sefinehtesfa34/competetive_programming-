from collections import Counter
def minWindow(S, T):
    memo = {}
    bestRight = len(S) + 1
    bestLeft = 0
    def dp(sPtr, tPtr):
        if tPtr == len(T):
            return sPtr - 1
        if sPtr == len(S):
            return len(S) + 1
        if (sPtr, tPtr) in memo:
            return memo[(sPtr, tPtr)]
        if S[sPtr] == T[tPtr]:
            memo[(sPtr, tPtr)] = dp(sPtr + 1, tPtr + 1)
            return memo[(sPtr, tPtr)]
        memo[(sPtr, tPtr)] = dp(sPtr + 1, tPtr)
        return memo[(sPtr, tPtr)]
    for index in range(len(S)):
        right = dp(index, 0)
        if bestRight - bestLeft > right - index and right < len(S):
            bestRight = right
            bestLeft = index
    return S[bestLeft: bestRight + 1] if bestRight <  len(S) else ''











        