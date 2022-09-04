def find_subsets(nums):
  subsets = [[]]
  index = 0
  while subsets and index < len(nums):
    size = len(subsets)
    for start in range(size):
      sub = list(subsets[start])
      sub.append(nums[index])
      subsets.append(sub)
    index += 1
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3,4])))


main()
