from itertools import combinations

n = 4
k = 2

combination = list(combinations(range(1,n+1),k))

print([tuple(_) for _ in combination])
