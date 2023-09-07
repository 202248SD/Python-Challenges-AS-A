import random
list = [random.randint(1,1000) for i in range(9)]
for i in range(len(list)):
  target = list[i]
  j = i - 1
  while j >= 0 and target < list[j]:
    temp = list[j]
    list[j] = target
    list[j+1] = temp
    j -= 1
print(list)
