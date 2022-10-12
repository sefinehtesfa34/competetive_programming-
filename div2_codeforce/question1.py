from typing import Counter
def finder():
    if nums1 == nums2:
        print(0)
        return 
    if sorted(nums1) == sorted(nums2):
        print(1)
        return 
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    contradict = 0
    for index in range(len(nums1)):
        if nums1[index] != nums2[index]:
            contradict += 1
    needed = abs(counter1[1]  - counter2[1])
    if needed == contradict:
        print(needed)
        return 
    print(needed + 1)
t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    finder()
    