print("----->TicTacToe<-----")
oxo = [["#","#","#"],["#","#","#"],["#","#","#"]]
def print_oxo():
  for i in range(3):
    print(*oxo[i])
def checkerX():
  for i in range(3):
    if oxo[i][0] == "X" and oxo[i][1] == "X" and oxo[i][2] == "X":
      print("Player 1 wins!")
      exit()
    elif oxo[0][i] == "X" and oxo[1][i] == "X" and oxo[2][i] == "X":
      print("Player 1 wins!")
      exit()
    elif oxo[0][0] == "X" and oxo[1][1] == "X" and oxo[2][2] == "X":
      print("Player 1 wins!")
      exit()
    elif oxo[2][0] == "X" and oxo[1][1] == "X" and oxo[0][2] == "X":
      print("Player 1 wins!")
      exit()

def checkerO():
  for i in range(3):
    if oxo[i][0] == "O" and oxo[i][1] == "O" and oxo[i][2] == "O":
      print("Player 1 wins!")
      exit()
    elif oxo[0][i] == "O" and oxo[1][i] == "O" and oxo[2][i] == "O":
      print("Player 1 wins!")
      exit()
    elif oxo[0][0] == "O" and oxo[1][1] == "O" and oxo[2][2] == "O":
      print("Player 1 wins!")
      exit()
    elif oxo[2][0] == "O" and oxo[1][1] == "O" and oxo[0][2] == "O":
      print("Player 1 wins!")
      exit()

def TicTacToe2p():
  print_oxo()
  for i in range(4):
    a = int(input("Player 1 input the column number you want to put X in [0,1,2]:"))
    b = int(input("Player 1 input the row number you want to put X in [0,1,2]:"))
    while oxo[a][b] != "#":
      print("Try a valid cell!")
      a = int(input("Player 1 input the column number you want to put X in [0,1,2]:"))
      b = int(input("Player 1 input the row number you want to put X in [0,1,2]:"))
    else:
      oxo[a][b] = "X"
      print("-----")
      print_oxo()
      print("-----")
    checkerX()
    
    c = int(input("Player 2 input the column number you want to put X in [0,1,2]:"))
    d = int(input("Player 2 input the row number you want to put X in [0,1,2]:"))
    while oxo[c][d] != "#":
      print("Try a valid cell!")
      c = int(input("Player 2 input the column number you want to put X in [0,1,2]:"))
      d = int(input("Player 2 input the row number you want to put X in [0,1,2]:"))
    else:
      oxo[c][d] = "O"
      print("-----")
      print_oxo()
      print("-----")
    checkerO()
  a = int(input("Player 1 input the column number you want to put X in [0,1,2]:"))
  b = int(input("Player 1 input the row number you want to put X in [0,1,2]:"))
  while oxo[a][b] != "#":
    print("Try a valid cell!")
    a = int(input("Player 1 input the column number you want to put X in [0,1,2]:"))
    b = int(input("Player 1 input the row number you want to put X in [0,1,2]:"))
  else:
    oxo[a][b] = "X"
    print("-----")
    print_oxo()
    print("-----")
    for i in range(3):
      if oxo[i][0] == "X" and oxo[i][1] == "X" and oxo[i][2] == "X":
        print("Player 1 wins!")
        exit()
      elif oxo[0][i] == "X" and oxo[1][i] == "X" and oxo[2][i] == "X":
        print("Player 1 wins!")
        exit()
      elif oxo[0][0] == "X" and oxo[1][1] == "X" and oxo[2][2] == "X":
        print("Player 1 wins!")
        exit()
      elif oxo[2][0] == "X" and oxo[1][1] == "X" and oxo[0][2] == "X":
        print("Player 1 wins!")
        exit()
      else:
        print("Draw!")
  
    

TicTacToe2p()
#AS59
