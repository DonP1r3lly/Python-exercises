#pedir un numero por teclado y mostrar los 10
#primeros terminos de su tabla de multiplicar

numero=int(input("introduce un numero: "))

for i in range(1,11):
	print(numero, "x", i, "=", (numero*i))