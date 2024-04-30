# pedir 10 numeros por teclado. sumarlos y mostrar el
# resultado por pantalla.


suma=0
for n in range(0,10):
	numero=int(input("introduce un numero: "))
	suma= suma+ numero

print("la suma total es: ", suma)