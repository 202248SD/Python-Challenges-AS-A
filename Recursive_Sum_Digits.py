
def sumDigits(num):
  if num < 10:
    return num
  else:
    return num%10 + sumDigits(num//10)

