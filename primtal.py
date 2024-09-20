tal = int(input("Mata in ett tal: "))

primtal = True
for i in range(2,tal//2+1):
    if tal % i == 0:
        primtal = False
        break

if primtal:
    print("Primtal")
else:
    print("Inte primtal")