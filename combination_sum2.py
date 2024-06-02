def combinationSum(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], target - candidates[i])
    
    result = []
    backtrack(0, [], target)
    return result

# Test cases
print(combinationSum([2,3,6,7], 7))  # Output: [[2, 2, 3], [7]]
print(combinationSum([2,3,5], 8))     # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(combinationSum([2], 1))         # Output: []

