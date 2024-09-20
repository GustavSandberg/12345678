tal = []

while True:
    a = input("Mata in ett tal ansar skriv klar ")
    if a .lower() == ("klar"):
        break
    tal.append(int(a))
tal.sort()
print(tal)

if len(tal) % 2 == 0:
    i2 = len(tal)//2
    i1 = i2 - 1 
    median = (tal[i1] + tal[i2])/2
else:
    i = len(tal)//2
    median = tal[1]

max = max(tal)
min = min(tal)
sum = sum(tal)
medel = sum/len(tal)

print(f"Summan av listan är", sum)
print(f"Högsta talet i listan är", max)
print(f"Minsta talet i listan är", min)
print(f"Medelvärder av lsitan är", medel)
print(f"Medianen av talen i slistan är", median)