#Write a Python program to calculate the sum of three
# given numbers, if the values are equal then return 
#thrice of their sum

def sumadetres(x,y,z):

	sum= x+y+z

	if x==y==z:
		sum=sum*3

	return sum

print(sumadetres(1,5,7))
print(sumadetres(5,5,5))


