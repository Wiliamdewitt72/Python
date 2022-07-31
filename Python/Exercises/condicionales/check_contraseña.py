# Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = "pollofrito414"

password_check = str(input("Escriba la contraseña: ")).lower()
# Se usa la función 'str()' en caso de que el usuario introduzca un número.
# Se usa el método '.lower()', para hacer todo lo introducido minusculas y poder así compararlo.
if password_check == password:
    print("Las contraseñas coinciden :D")
else:
    print("Las contraseñas no coinciden :(")
