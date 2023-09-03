import random
number = random.randint(1,111)
min = 1
max = 111
mid = (min+max)/2
guess = 0
while number != mid:
  print("Guess number", guess+1,"is",mid)
  if number < mid:
    max = mid
    mid  = round((min+mid)/2)
    guess += 1
    print("number is lower!")
  elif number > mid:
    min = mid
    mid = round((max+mid)/2)
    guess += 1
    print("number is higher!")
  else:
    print("error")
print("The answer was",number)
print("The total number of guesses was",1+guess)
