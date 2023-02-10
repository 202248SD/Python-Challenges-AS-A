import random
list = [random.randint(1,100) for i in range(9)]
#list = [9,8,7,6,4,3,2]
print("original list",list)
n = len(list)-1
for i in range(n):
  for x in range(n-i):
    if list[x] > list[x+1]:
      a = list[x]
      list [x] = list[x+1]
      list[x+1] = a
print("sorted list",list)
#CREDIT TO GYOCHAN KYU FOR TELLING ME THE LINE 2 THING VERY NICE 
#AS01
