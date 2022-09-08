def get_different_number(arr):
    #set_nums = set(arr)
    #for index in range(len(arr)):
     # if index not in set_nums:
      #    return index
    #return len(arr)
    index = 0
    while index < len(arr):
      while arr[index] != index and arr[index] < len(arr):
        num = arr[index]
        arr[index],arr[num] = arr[num], arr[index]
      index += 1
    for index in range(len(arr)):
      if index != arr[index]:
        return index
    return len(arr)
  
#     Getting a Different Number
# Given an array arr of unique nonnegative integers, implement a function getDifferentNumber 
# that finds the smallest nonnegative integer that is NOT in the array.

# Even if your programming language of choice doesn’t have that restriction (like Python), 
# assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, 
# the operation MAX_INT + 1 would be undefined in our case.

# Your algorithm should be efficient, both from a time and a space complexity perspectives.

# Solve first for the case when you’re NOT allowed to modify the input arr. If successful 
# and still have time, see if you can come up with an algorithm with an improved space complexity 
# when modifying arr is allowed. Do so without trading off the time complexity.

# Analyze the time and space complexities of your algorithm.