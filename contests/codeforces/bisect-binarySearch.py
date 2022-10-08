from bisect import bisect_left, bisect_right
stack = [1, 2, 2]
index = bisect_left(stack, 2)
print(index)
index = bisect_right(stack, 2)
print(index)