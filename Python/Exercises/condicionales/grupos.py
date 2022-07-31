# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
letrasA = list("abcdefghijklm")
letrasB = list("nopqrstuvwxyz")

nombre = list(str(input("Introduzca su nombre: ")).lower())
sexo = str(input("Introduzca su sexo (masculino o femenino): ")).lower()

if (sexo == "masculino") and (nombre[0] in letrasB):
    print("Asignado al grupo A")
elif (sexo == "femenino") and (nombre[0] in letrasA):
    print("Asignado al grupo A")
elif (sexo == "masculino") or (sexo == "femenino"):
    print("Asignado al grupo B")
else:
    print("Nombre o Sexo incorrectos.")
