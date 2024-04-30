#pedir dos numeros por teclado. Si el primero es mayor
#que el segundo, intercambiarlos.

num1=int(input("introduce un numero: "))
num2=int(input("introduce otro numero: "))

print("num1 es", num1, "y", "num2 es", num2)

if num1>num2:
 	variable= num1
 	num1=num2
 	num2=variable

print("num1 es", num1, "y", "num2 es", num2)
