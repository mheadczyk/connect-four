board_array = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

#print array
def print_board():
  print("  1   2   3   4   5   6   7\n+---+---+---+---+---+---+---+")
  for lst in board_array:
    print('| ', end='')
    for item in lst:
      print(item, end=' | ')
    print('\n+---+---+---+---+---+---+---+')

#insert x or o in any given column
def insert(column, piece):
  if piece not in 'xXoO':
    print("Niepasujący element! Tylko X i O!")
    return None
  if column not in [1,2,3,4,5,6,7]:
    print("Zła kolumna!")
    return None
  if (board_array[0][column-1] != ' '):
    print("Kolumna jest pełna!")
    return None
  for i in range(1,7):
    if (board_array[-i][column-1] != ' '):
      continue
    else:
      board_array[-i][column-1] = piece.upper()
      return None

#if no more moves left return true
def no_more_moves():
  for row in board_array:
    for item in row:
      if item == ' ':
        return False
  return True

#define if given piece won
def winning(piece):
  #horizontal
  for row in range(6):
    for item in range(4):
      if board_array[row][item] == piece and board_array[row][item+1] == piece and board_array[row][item+2] == piece and board_array[row][item+3] == piece:
        return True
  #vertical
  for row in range(3):
    for item in range(7):
      if board_array[row][item] == piece and board_array[row+1][item] == piece and board_array[row+2][item] == piece and board_array[row+3][item] == piece:
        return True
  #diagonal
  for x in range(len(board_array) - 3):
    for y in range(3, len(board_array[0])):
      if board_array[x][y] == piece and board_array[x + 1][y - 1] == piece and board_array[x + 2][y - 2] == piece and board_array[x + 3][
        y - 3] == piece:
        return True
  for x in range(len(board_array) - 3):
    for y in range(len(board_array[0]) - 3):
      if board_array[x][y] == piece and board_array[x + 1][y + 1] == piece and board_array[x + 2][y + 2] == piece and board_array[x + 3][
        y + 3] == piece:
        return True
  return False

def play_game():
  game_on = True
  while game_on == True:
    print_board()
    print("Gracz X: Wybierz kolumnę do wrzucenia klocka (od 1 do 7):")
    gracz1 = input()
    insert(int(gracz1), "X")
    print_board()
    if winning("X") == True:
      print("Gracz X wygrał!")
      return None
    print("Gracz O: Wybierz kolumnę do wrzucenia klocka (od 1 do 7):")
    gracz2 = input()
    insert(int(gracz2), "O")
    print_board()
    if winning("O") == True:
      print("Gracz O wygrał!")
      return None

play_game()