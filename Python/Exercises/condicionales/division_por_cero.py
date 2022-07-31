# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero1 = int(input("Introduzca el primer número: "))
numero2 = int(input("Introduzca el segundo número: "))

if numero2 == 0:
    print("Por si no lo sabías intentas dividir por cero.\nY eso no me agrada >:0")
else:
    print("El resultado de la división es: ", numero1 /
          numero2, "\nGracias por su visita vuelva pronto :)")
