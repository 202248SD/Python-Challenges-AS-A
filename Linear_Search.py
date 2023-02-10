list = [1,2,325,53,436,2,32,2,12,6,8,4,1]
a = int(input("input the number you want to find in the list:"))
b = False
for i in range(len(list)):
  if a == list[i]:
    print("the number was found and the index is",i,)
    b = True
    break
if b == False:
  print("the number wasn't found in the list")
  #AS02
