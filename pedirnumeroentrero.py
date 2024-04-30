#pedir un numero entero al usuario e indicar si es par

# %=Operador módulo. Obtiene el resto de dividir el 
# operando de la izquierda por el de la derecha.


num1=int(input("introduce un numero: "))

if num1 % 2==0:
	print("el numero es par")
else:
	print("el numero es impar")



print("es par") if num1 % 2==0 else print("es impar")


