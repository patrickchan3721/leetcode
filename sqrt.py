import math

def mySqrt(x: int):
  if x == 1:
    return 1
  sqrt = x // 2
  upper = x
  lower = 0
  while upper - lower >= 0.5:
    print(lower, upper, sqrt)
    if sqrt * sqrt > x:
      upper = sqrt
      sqrt = (sqrt - lower) / 2 + lower
    elif sqrt * sqrt < x:
      lower = sqrt
      sqrt = (upper - sqrt ) / 2 + lower
    else:
      return int(sqrt)

  if math.floor(upper) == math.floor(lower) + 1:
    if math.floor(upper) ** 2 <= x:
      return math.floor(upper)
    else:
      return math.floor(lower)
  else:
    return math.floor(lower)

inputText = ""
while inputText != 'q':
  inputText = input("Please enter an integer: ")
  if inputText.isdigit():
    print(mySqrt(int(inputText)))
