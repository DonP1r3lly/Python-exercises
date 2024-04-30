"""
descuentos de navidad de acuerdo a su monto de compra.

"""

nombre=input("introduce tu nombre: ")
valorcompra= float(input("introduce el valor de tu compra: "))
descuento=0

if valorcompra<80:
	descuento=0
elif valorcompra<80 and valorcompra<150:
	descuento=0.10
elif valorcompra>=150 and valorcompra<=300:
	descuento=0.15
elif valorcompra>300 and valorcompra<500:
	descuento=0.20

descontadofinal= valorcompra*descuento
preciofinal= valorcompra- descontadofinal

print("tu nombre es:", nombre)
print("el valor de tu compra es: ", valorcompra, "euros")
print("el valor de tu compra con el descuento es:", preciofinal, "euros")