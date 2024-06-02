s = "qbmhukucteihghldwdobtvgwwnhflpceiwhbkmvxavmqxedfndegztlpjptpdowwavemasyrjxxnhldnloyizyxgqlhejsdylvkpdzllrzoywfkcamhljminikvwwvqlerdilrdgzifojjlgeayprejhaequyhcohoeonagsmfrqhfzllobwjhxdxzadwxiglvzwiqyzlnamqqsastxlojpcsleohgtcuzzrvwzqugyimaqtorkafyebrgmrfmczwiexdzcokbqymnzigifbqzvfzjcjuugdmvegnvkgbmdowpacyspszvgdapklrhlhcmwkwwqatfswmxyfnxkepdotnvwndjrcclvewomyniaefhhcqkefkyovqxyswqpnysafnydbiuanqphfhfbfovxuezlovokrsocdqrqfzbqhntjafzfjisexcdlnjbhwrvnyabjbshqsxnaxhvtmqlfgdumtpeqzyuvmbkvmmdtywquydontkugdayjqewcgtyajofmbpdmykqobcxgqivmpzmhhcqiyleqitojrrsknhwepoxawpsxcbtsvagybnghqnlpcxlnshihcjdjxxjjwyplnemojhodksckmqdvnzewhzzuswzctnlyvyttuhlreynuternbqonlsfuchxtsyhqlvifcxerzqepthwqrsftaquzuxwcmjjulvjrkatlfqshpyjsbaqwawgpabkkjrtchqmriykbdsxwnkpaktrvmxjtfhwpzmieuqevlodtroiulzgbocrtiuvpywtcxvajkpfmaqckgrcmofkxynjxgvxqvkmhdbvumdaprijkjxxvpqnxakiavuwnifvyfolwlekptxbnctjijppickuqhguvtoqfgepcufbiysfljgmfepwyaxusvnsratn"

def longestPaldinrome(s):
  max_length = 0
  max_string = ""
  for i in range(len(s)):
    if len(s) - i < max_length:
      return max_string

    for j in range(len(s),i-1,-1):
      if len(s[:j]) == 1:
        break
      if len(s[i:j]) % 2 == 0:
          #print(s[i:i+len(s[i:j])//2], s[i+len(s[i:j])//2:j])
          print(s[i:i+len(s[i:j])//2], s[j-1:i+len(s[i:j])//2-1:-1])
          if s[i:i+len(s[i:j])//2] ==  s[j-1:i+len(s[i:j])//2-1:-1]:
            if len(s[i:j]) > max_length:
              max_length = len(s[i:j])
              max_string = s[i:j]
              break
      else:
          #print(s[i:i+len(s[i:j])//2], s[i+len(s[i:j])//2+1:j])
          print(s[i:i+len(s[i:j])//2], s[j-1:i+len(s[i:j])//2:-1])
          if s[i:i+len(s[i:j])//2] == s[j-1:i+len(s[i:j])//2:-1]:
            if len(s[i:j]) > max_length:
              max_length = len(s[i:j])
              max_string = s[i:j]
              break
  if max_length == 0:
    return s[0]
  return max_string

print(longestPaldinrome(s))
