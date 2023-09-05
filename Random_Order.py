import random
floors = int(input("how many floors does your building have?"))
print("The guards will be visiting each floor in this assigned order:")
print(random.sample(list(range(1,floors+1)),floors))
