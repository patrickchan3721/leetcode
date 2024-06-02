def countPrimes(n):
  arr = [2, 3] + [ x for x in range(4,n) if x % 2 !=0 and x % 3 != 0 ]
  for i in arr[1:]:
    for j in range(2, (i//2)+1):
      print(arr) 
      if i % j == 0:
        arr.remove(i)
        break
  return len((arr))

print(countPrimes(499979))
