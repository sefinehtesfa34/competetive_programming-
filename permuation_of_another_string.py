from typing import Counter


class Solution:
    def anagramOfAnother(self, str1, string):
        hashmap  = Counter()
        counter = Counter(str1)
        used = left = 0
        for index in range(len(string)):
            if string[index] not in counter:
                left = index + 1
                used = 0
                hashmap = Counter()
                continue
            hashmap[string[index]] += 1
            while hashmap[string[index]] > counter[string[index]]:
                hashmap[string[left]] -= 1
                left += 1
            used += int(hashmap[string[index]] == counter[string[index]]) if used != len(counter) else 0
            if used == len(counter):
                print(left, index) 
                
solution = Solution()
str1 = input()
string = input()
result = solution.anagramOfAnother(str1, string)
print(result)