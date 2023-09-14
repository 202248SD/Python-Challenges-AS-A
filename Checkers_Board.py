n, m = int(input("input length of board")), int(input("input width of board"))
board = []
for i in range(n):
  temp = []
  for j in range(m):
    if i % 2 ==0:
      if j % 2 == 0:
        temp.append(".")
      else:
        temp.append("*")
    else:
      if j % 2 == 1:
        temp.append(".")
      else:
        temp.append("*")
  board.append(temp)
for i in range(n):
  print(*board[i])
