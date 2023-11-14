preferences = [
  [0,1,2],
  [2,1,0],
  [0,2,1],
  [1,2,0],
  [1,0,2],
]
winner = False
A = 0
B = 0
C = 0
total_votes = len(preferences)

while winner == False:
  for i in preferences:
    if i[0] == 0:
      A += 1
    if i[0] == 1:
      B += 1
    if i[0] == 2:
      C += 1
  if A > total_votes * 0.5:
    winner = True
    print("A")
    break
  if B > total_votes * 0.5:
    winner = True
    print("B")
    break
  if C > total_votes * 0.5:
    winner = True
    print("C")
    break
  if A==B==C:
    winner = True
    print("Tie")
    break
  off = []
  if A<B and A<C:
    off.append(0)
  if B<A and B<C:
    off.append(1)
  if C<A and C<B:
    off.append(2)
  if A==B and C>A:
    winner = True
    print("C")
    break
  if A==C and B>A:
    winner = True
    print("B")
    break
  if B==C and A>B:
    winner = True
    print("A")
    break
  for i in preferences:
    for j in off:
      i.remove(j)
  A = 0
  B = 0
  C = 0
