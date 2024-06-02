roman_dict = {1: 'I',
              4: 'IV',
              5: 'V',
              9: 'IX',
              10: 'X',
              40: 'XL',
              50: 'L',
              90: 'XC',
              100: 'C',
              400: 'CD',
              500: 'D',
              900: 'CM',
              1000: 'M'}

n =  88

for key,value in dict(reversed(list(roman_dict.items()))).items():
  if n < key:
    continue
  else:
    print(n // key * value, end='')
    n -= n // key * key

print()
