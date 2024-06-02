strs = ["flower", "flow", "flight"]
common_prefix = ""
  
if len(strs) == 1:
  return strs[0]

try:
  for j in range(max( [ len(k) for k in strs ] )):
    for i in range(len(strs) - 1):
      if strs[0][0:j+1] != strs[i+1][0:j+1]:
        raise StopIteration
      else:
        if i == len(strs) - 2:
          common_prefix = strs[0][0:j+1]

except StopIteration:
  pass

print(common_prefix)
