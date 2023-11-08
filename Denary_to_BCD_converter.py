denary = list(input("Put your denary number here:"))
binary = []

for i, j in enumerate(denary):
  binary.append(bin(int(j)))
  binary[i] = binary[i][2:]
  while len(binary[i]) < 4:
    binary[i] = "0"+binary[i]

print(*binary)
