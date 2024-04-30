#loteria 

numeros=[]
for i in range(6):
	#append es para añadir elementos a la lista
	numeros.append(int(input("introduce un numero: ")))


#sort es para ordenar los numeros
numeros.sort()
print("los numeros ganadores son: ", numeros)