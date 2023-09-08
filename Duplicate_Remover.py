def duplicate_remover(list):
  print("list w/ duplicates:",list)
  output_list = []
  for i in list:
    if i not in output_list:
      output_list.append(i)
  print("List w/o duplicates:",output_list)
import random
numbers = [random.randint(1,6) for i in range(5)]
duplicate_remover(numbers)
