def two_sum(nums, target):
  nums_index = {}

  for i, j in enumerate(nums):
    complement = target - j
    if complement in nums_index:
      return [ nums_index[complement], i ]
    nums_index[j] = i
  
nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))
