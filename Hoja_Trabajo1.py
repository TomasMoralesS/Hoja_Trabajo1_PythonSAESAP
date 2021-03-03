#mensaje inicial
print("\n----------------------Bienvenido----------------------")
print("     Digita tu estatura en metros  (m)  ")
estatura = int (input(">"))
print ("")
print("     Digita tu peso en kilogramos (kg)    ")
Peso = int (input(">"))
print ("")
IMS = (estatura//(Peso**2)) 
print("Tu indice de masa corporal es : ",IMS)

print("------------------------------------------------------")