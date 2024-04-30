#calculadora de indice de masa corporal (IMC)

print("calculadora de indice de masa corporal (IMC")

contador=0

while contador!=2:

	contador= int(input("¿quieres seguir calculando el imc? 1.Si y 2.No"))

	if contador==1:
		estatura=float(input("introduce tu estatura: "))
		peso=float(input("introduce tu peso: "))

		resultado= round(peso/(estatura**2),2)

		if resultado<18.5:
			print("IMC", resultado, "= BAJO DE PESO")
		elif 18.5< resultado<24.99:
			print("IMC", resultado, "= PESO NORMAL")
		elif 25< resultado<30:
			print("IMC", resultado, "= SOBREPESO")
		elif resultado>30:
			print("IMC", resultado, "= OBESIDAD")

	elif contador==2:
		print("hasta pronto")

print("gracias por usar la calculadora de IMC")