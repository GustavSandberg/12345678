berries = ["Blåbär","hallon","björnbär","banan","konkelbär" ,"laxbär"]

berries.append("lingon")
berries.insert(6,"hjortron")
berries.remove("konkelbär")

for berry in berries:
    print(berry,end=" ")