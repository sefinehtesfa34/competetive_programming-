from collections import Counter


n = int(input())
flats = input()
left = 0
right = 0
count = len(set(flats))
minLength = n 
hashmap = Counter()
while right < len(flats):
    hashmap[flats[right]] += 1
    while len(hashmap) == count and left < len(flats):
        hashmap[flats[left]] -= 1
        if hashmap[flats[left]] == 0:
            del hashmap[flats[left]]
        minLength = min(minLength, right - left + 1)
        left += 1
    right += 1
print(minLength)
    