#pedir dos numeros al usuario e indicar si el primero es
#multiplo del segundo. En caso contrario, comprobar si
#el segundo es multiplo del primero.

# %=Operador módulo. Obtiene el resto de dividir el 
# operando de la izquierda por el de la derecha.


num1=int(input("introduce un numero: "))
num2=int(input("introduce otro numero: "))


if num1 % num2 ==0:
	print(num1, "es multiplo de ", num2)
elif num2 % num1 ==0:
	print(num2, "es multiplo de ", num1)
else:
	print("no son multiplos")
