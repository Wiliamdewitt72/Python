print("Hello world!")
#-----------------------------------------------------------------
# --- Variables ---
# ----------------------------------------------------------------

sum = 1 + 2
#Las variables pueden almacenar lo que sea, hasta returns de funciones.
producto = sum * 2
producto = producto + producto
#También estar definidas mediante otras variables o redefinirse.

print(producto)
#Así se imprime una variable.

#----------------------------------------------------------------
# --- Tipos de datos ---
#----------------------------------------------------------------

# Números 
numero_entero = 9 #int

cumpleaños = 3.12 #float

numero_complejo = 5j #complex

verdad_o_falso = True #boolean

una_palabra = "palabra" #str, es una cadena

tipo = type(numero_complejo) #Sirve para conocer el tipo de dato de la variable. 

print(tipo)

#----------------------------------------------------------------
# --- Operadores ---
#----------------------------------------------------------------

x = 4
y = 5
z = 7j
f = 4.1

print(x + y) #entero + entero = entero

print(z + f) #complejo + flotante = complejo

print(x + f) #entero + complejo = flotante

# Conclusión: Los tipos de datos númericos se pueden sumar sin embargo hay que tener cuidado con los tipos complex.



