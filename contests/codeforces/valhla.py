from itertools import accumulate


n, m = list(map(int, input().split()))
warrior_strength = list(map(int, input().split()))
arrows = list(map(int, input().split()))
prefix = list(accumulate(warrior_strength, initial = 0))
curSum = 0
def binarySearch(curSum):
        if curSum >= prefix[-1]:
            print(n)
            return -1
        left = 0
        right = n 
        while left <= right:
            mid = (left + right)//2
            if prefix[mid] < curSum:
                left = mid + 1
            else:
                right = mid - 1
        answer = n - left if curSum == prefix[left] else n - left + 1
        print(answer)
        return curSum 
for arrow in arrows:
    curSum += arrow
    flag = binarySearch(curSum)
    if flag == -1:
        curSum = 0