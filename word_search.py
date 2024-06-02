#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCCED"
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

def word_search(board, word):
  width = len(board)
  height = len(board[0])
  orig_board = board

  def backtrack(character_pos):
    print(character_pos, word[character_pos], current_pos[0], current_pos[1])
    if current_pos[1]-1 >= 0 and word[character_pos] == board[current_pos[0]][current_pos[1]-1]:
      board[current_pos[0]][current_pos[1]] = ''
      current_pos[1] = current_pos[1] - 1 
      character_pos += 1
      if character_pos == len(word): 
        return True
      if backtrack(character_pos):
        return True
    if current_pos[0]+1 < width and word[character_pos] == board[current_pos[0]+1][current_pos[1]]:
      board[current_pos[0]][current_pos[1]] = ''
      current_pos[0] = current_pos[0] + 1 
      character_pos += 1
      if character_pos == len(word): 
        return True
      if backtrack(character_pos):
        return True
    if current_pos[1]+1 < height and word[character_pos] == board[current_pos[0]][current_pos[1]+1]:
      board[current_pos[0]][current_pos[1]] = ''
      current_pos[1] = current_pos[1] + 1 
      character_pos += 1
      if character_pos == len(word): 
        return True
      if backtrack(character_pos):
        return True
    if current_pos[0]-1 >=0 and word[character_pos] == board[current_pos[0]-1][current_pos[1]]:
      board[current_pos[0]][current_pos[1]] = ''
      current_pos[0] = current_pos[0] -1
      character_pos += 1
      if character_pos == len(word): 
        return True
      if backtrack(character_pos):
        return True
    return False

  starting_point = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == word[0]:
        starting_point.append((i,j))

  if not starting_point:
    return False
  elif len(board) == 1 and len(word) == 1:
    return True

  for k,l in starting_point:
    current_pos = [ k,l ]
    board = orig_board
    if backtrack(1):
      return True
  return False
    
print(word_search(board, word))
