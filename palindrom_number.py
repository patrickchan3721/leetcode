x = 10101

s = str(x)
half = len(s) // 2

if len(s) % 2 == 0:
  print(s[:half] == s[:half-1:-1])
else:
  print(s[:half] == s[:half:-1])
