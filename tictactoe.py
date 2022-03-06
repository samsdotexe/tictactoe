import os

def clear_screen():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

clear_screen()

board = [ [ "1", "2", "3" ],
          [ "4", "5", "6" ],
          [ "7", "8", "9" ] ]

angles  = [ [ "", "", "" ], [ "", "", "" ] ]

columns = [ [ "", "", "" ],
            [ "", "", "" ],
            [ "", "", "" ] ]

def print_board():
    a, b = 0, -1
    while a < 3 and b > -3:
        for row in board:
            angles[0][a] += row[a]
            angles[1][b] += row[b]

            print(row)
            a, b = a + 1, b - 1

print("board:")
print_board()
print("angles:")
print(angles)
print("columns:")
print(columns)
