vowels = ["a","e","i","o","u"]


def make_it_laugh(strings):
  new = list(strings)
  for i in range(len(new)):
    if new[i] in vowels:
      new[i] = "haha"
  print(strings)
  print("".join(new))

make_it_laugh("wow")
