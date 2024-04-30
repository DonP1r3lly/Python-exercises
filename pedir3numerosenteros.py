#pedir 3 numeros enteros al usuario y mostrar por 
#pantalla el mayor de los tres


num1=int(input("introduce un numero: "))
num2=int(input("introduce un segundo numero: "))
num3=int(input("introduce un tercer numero: "))

if num1>num2 and num1>num3:
	print("el numero mayor es: ",num1)
elif num2>num1 and num2>num3:
	print("el numero mayor es: ",num2)
else:
	print("el numero mayor es: ",num3)