Växjö = int(input("Hur varmt är det i Växjö?: "))
Kalmar = int(input("Hur varmt är det i Kalmar?: "))
Jönköping = int(input("Hur varmt är det i Jönköping?: "))

if Växjö > Kalmar and Växjö > Jönköping:
    print("Växjö är varmast!")

elif Kalmar > Växjö and Kalmar > Jönköping:
    print("Kalmar är varmast!")

else:
    print("Jönköping är varmast!")