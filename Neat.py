for i in range(101,1000):
  a = list(str(i))
  sum = 0
  for j in range(len(a)):
    sum += int(a[j])
  if i % sum == 0:
    print(i)
