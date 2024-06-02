import re

def isPalindrome(s: str):
  s = re.sub(r'[^a-zA-Z0-9]','', s.lower())
  if len(s) % 2 == 0:
    #print(s[:len(s)//2], s[:len(s)//2-1:-1])
    return s[:len(s)//2] == s[:len(s)//2-1:-1]
  else:
    #print(s[:len(s)//2], s[:len(s)//2:-1])
    return s[:len(s)//2] ==  s[:len(s)//2:-1]

s = "A man, a plan, a canal: Panama"
#s = "abcde"
#s = "abcd"
print(isPalindrome(s))
