vowels = ["a", "e", "i", "o", "u"]
text = list(str(input("What do you want to convert into Rövarspråket?")))
for i in enumerate(text):
  if i[1] not in vowels:
    text[i[0]] = str(i[1]) + "o" + str(i[1])
  print(text[i[0]],end="")
    
