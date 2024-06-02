from collections import defaultdict

candidates = [ 2,3,6,7 ]
target = 7

candidates2 = defaultdict(list)

for i in candidates:
  multiplier = 1
  while i * multiplier <= target:
    candidates2[i].append(i * multiplier)
    multiplier += 1

print(dict(candidates2))
