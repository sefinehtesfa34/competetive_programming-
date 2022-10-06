class Solution:
    def subarray(self, word):
        if not word:
            return 0
        left = right = result = 0
        count = [0, 0, 0]
        end = len(word)
        while right < len(word):
            count[ord(word[right]) - ord('a')] += 1 
            while count[0] and count[1] and count[2]:
                count[ord(word[left]) - ord('a')] -= 1
                result += end - right
                left += 1
            right += 1
        return result 
solution = Solution()
word = input()
result = solution.subarray(word)
print(result)
'''
welcome  conatins three vowels 2e and one o characters

we =  1
wel = 1
welc = 1
welco = 2
welcom = 2
welcome = 3
el = 1
elc = 1
elco = 2
elcom = 2
elcome = 3
lco = 1
lcom = 1
lcome = 2
co = 1
com = 1
come = 2
o = 1
om = 1
ome = 2
me = 1
e = 1

0 1 2 3 4 5 6 7 8 9

'''