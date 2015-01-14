import numpy as np
n=input()
m=input()
i=1
num_gen=np.zeros(m)
num_gen[m-1]=1
while 1:
	i=i+1
	j=0
	temp=num_gen
	sum1=0
	while 1:
		sum1=sum1+temp[j]
		if j== m-2:
			break	
		j=j+1
	j=0
	while 1:
		num_gen[j]=num_gen[j+1]
		if j == m-2:
			break
		j=j+1
	num_gen[m-1]=sum1	
	print "%.0f" % sum(num_gen)	
	if i==n	:
		break
sum1=0
j=0
while 1:
	sum1=sum1+num_gen[j]	
	if j==m-1:
		break
	j=j+1

print "%.1f" % sum1
#print num_gen

