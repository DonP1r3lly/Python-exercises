# Mean
list1= [12,16,20,12,30,25,23,24,20]
mean= sum(list1)/len(list1)
print(mean)

# Median
list1= [12,16,20,12,30,25,23,24,20]
list1.sort()

if len(list1) % 2 ==0:
	m1= list1[len(list1)//2]
	m2= list1[len(list1)//2-1]
	median= (m1+m2)/2
else:
	median=list1[len(list1)//2]
print(median)

#Mode
list1= [12,16,20,12,30,25,23,24,20]
frecuency= {}
for i in list1:
	frecuency.setdefault(i, 0)
	frecuency[i]+1

frequent= max(frecuency.values())
for i, j in frecuency.items():
	if j == frequent:
		mode=i
print(mode)