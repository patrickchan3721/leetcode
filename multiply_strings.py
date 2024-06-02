str1, str2 = "123", "456"

def convert_str_to_int(str_1):
  sum = 0
  multiplier = 1
  for i in range(len(str_1)-1,-1,-1):
    sum += (ord(str_1[i])-48) * multiplier
    multiplier *= 10
  return sum

def convert_int_to_str(num_1):
  result_str = ""
  multiplier = 10
  while num_1 >= 0:
    result_str = chr(num_1 % multiplier + 48) + result_str
    num_1 = num_1 // 10
  return result_str


print(convert_int_to_str(convert_str_to_int(str1) * convert_str_to_int(str2)))
