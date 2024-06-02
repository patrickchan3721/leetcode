a = "1010"
b = "1011"

max_length = max(len(a), len(b))
a = "0" * (max_length - len(a)) + a
b = "0" * (max_length - len(b)) + b
plus = 0
sum = ""

for i in range(max_length-1,-1,-1):
  try:
    a_digit = int(a[i])
  except:
    a_digit = 0
  try:
    b_digit = int(b[i])
  except:
    b_digit = 0
  
  sum_digit = a_digit + b_digit + plus
  
  if sum_digit == 3:
    plus = 1
    sum = '1' + sum
  elif sum_digit == 2:
    plus = 1
    sum = '0' + sum
  elif sum_digit == 1:
    plus = 0
    sum = '1' + sum
  else:
    plus = 0
    sum = '0' + sum

if plus == 1:
  sum = '1' + sum
print(sum)
