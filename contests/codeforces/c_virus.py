from typing import Counter


t = int(input())
for _ in range(t):
  n, c = list(map(int, input().split()))
  orbits = list(map(int, input().split()))
  hashmap = Counter(orbits)
  result = 0
  for planet in hashmap:
    result += min(hashmap[planet], c)
  print(result)
  