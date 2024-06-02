l1 = [2,4,3]
l2 = [5,6,4]
l = []
add_one = 0

for i in range(max(len(l1),len(l2))):
  if i >= len(l1):
    l.append(l2[i] + add_one)
    add_one = 0
  elif i >= len(l2):
    l.append(l1[i] + add_one)
    add_one = 0
  else:
    if l1[i] + l2[i] > 9:
      l.append(l1[i] + l2[i] - 10 + add_one)
      add_one = 1
    else:
      l.append(l1[i] + l2[i] + add_one)
      add_one = 0

#l = l[::-1]
print(l)
