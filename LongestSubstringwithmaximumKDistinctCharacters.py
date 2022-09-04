from queue import deque
from collections import defaultdict
def longest_substring_with_k_distinct(str1, k):
    queue = deque([])
    right = max_len = result = 0
    dict = defaultdict(int)
    while right < len(str1):
      char = str1[right]
      queue.append(char)
      dict[char] += 1
      result += 1
      while len(dict) == k + 1:
          front = queue.popleft()
          dict[front] -= 1
          if dict[front] == 0:
            del dict[front]
          result -= 1
      if len(dict) <= k:
        max_len = max(result, max_len)
      right += 1
    return max_len
