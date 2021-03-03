#mensaje inicial
print("\n----------------------Bienvenido----------------------")
print("     Digita tu estatura en metros  (m)  ")
estatura = float (input(">"))
print ("")
print("     Digita tu peso en kilogramos (kg)    ")
Peso = float (input(">"))
print ("")
IMS = round( (estatura / (Peso**2) ) , 2 ) 
print("Tu índice de masa corporal es (IMC) : ",IMS)

print("------------------------------------------------------")
