Växjö = int(input("Vad är tempraturen i Växjö"))
Kalmar = int(input("Vad är tempraturen i Kalmar"))
Jönköping = int(input("Vad är tempraturen i Jönköping"))


if Växjö > Jönköping and Kalmar:
    print("Växjö är varmast")
elif Jönköping > Kalmar and Växjö:
    print("Jönköping är varmast")
elif Kalmar > Växjö and Jönköping:
    print("Kalmar är varmast") 
elif Växjö == Jönköping == Kalmar:
    print("Alla är lika varma")