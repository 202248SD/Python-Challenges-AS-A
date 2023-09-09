import random

ipv4 = []
for i in range(4):
  ipv4.append(random.randint(0, 255))
print(f"{ipv4[0]}.{ipv4[1]}.{ipv4[2]}.{ipv4[3]}")


ipv6 = []
for i in range(8):
  ipv6.append(str(hex(random.randint(0, 65535)))[2:6])
print(f"{ipv6[0]}:{ipv6[1]}:{ipv6[2]}:{ipv6[3]}:{ipv6[4]}:{ipv6[5]}:{ipv6[6]}:{ipv6[7]}")
