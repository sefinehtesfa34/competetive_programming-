import sys
from math import inf
def solution(A):
  if len(A) < 4:
    return -1
  values = []
  hashmap = {}
  answer = inf
  for val in A:
    if val in hashmap:
      hashmap[val] += 1
    else:
      hashmap[val] = 1
  for key, val in hashmap.items():
    if val >= 4:
      return 0
    if val >= 2:
      values.append(key)
  values.sort()
  for index in range(1, len(values)):
    answer = min(answer, values[index] - values[index - 1])
  if answer == inf:
    return -1
  return answer
