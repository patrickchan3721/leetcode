def searchRange(nums, target)
  left = 0
  right = len(nums)
  while True:
    mid = right // 2
    first = mid
    last = mid
    while target == nums[mid]:
      first -= 1
    while target == nums[mid]:
      last += 1
    if first and last:
      return [first, last]
    if target > nums[mid]:
      left = mid
    if target < nums[mid]:
      right = mid
