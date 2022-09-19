from collections import deque
def find_permutations(nums):
  result = deque([[]])
  for num in nums:
    size = len(result)
    for _ in range(size):
      front = list(result.popleft())
      for index in range(len(front) + 1):
        temp = list(front)
        temp.insert(index,num)
        result.append(list(temp))
  return result





def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3,4, 5])))

main()


