#pedir dos numeros por teclado y mostrar todos los 
#numeros pares compredidos entre ambos

num1=int(input("introduce un numero: "))
num2=num1
while num2 <= num1:
	num2=int(input("introduce otro numero: "))

for n in range(num1,num2+1):
	if n % 2 ==0:
		print(n)
