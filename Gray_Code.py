num = int(input("how many bits do you want?"))
out = ["0", "1"]
temp = []
for i in range(num-1):
    temp = out[::-1]
    for j in range(len(out)):
        out[j] = "0" + out[j]
        temp[j] = "1" + temp[j]
    out.extend(temp)
if num <= 0:
    print([])
else:
    print(out)
