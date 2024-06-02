def generate_combinations(arr1, arr2, index1, index2, combination, result):
    if sum(combination) < 0:
        return

    if index1 == len(arr1) and index2 == len(arr2):
        result.append(combination[:])  # Append a copy of the current combination
        return

    if index1 < len(arr1):
        combination.append(arr1[index1])
        generate_combinations(arr1, arr2, index1 + 1, index2, combination, result)
        combination.pop()  # Backtrack

    if index2 < len(arr2):
        combination.append(arr2[index2])
        generate_combinations(arr1, arr2, index1, index2 + 1, combination, result)
        combination.pop()  # Backtrack

n = 3
arr1 = [1] * n
arr2 = [-1] * n
result = []

generate_combinations(arr1, arr2, 0, 0, [], result)

string = ""
for combination in result:
    print(combination)
    '''
    for digit in combination:
        if digit == 1:
            string += '('
        elif digit == -1:
            string += ')'
    print(string)
    string = ""
    '''
