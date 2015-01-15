import numpy as np
file=open("rosalind_subs.txt","r")
lines=file.readlines()
print lines[0]
#print lines[1]
a=len(lines[0])-1
b=len(lines[1])-1
A=np.zeros(shape=a)
B=np.zeros(shape=b)
A=lines[0]
B=lines[1]
def equal(A,B):
	flag=1
	global b
	#print A,B,b
	for i in range (0,b):
		#print A[i],i
		if A[i]!=B[i]:
			flag=0	
	return flag
for i in range (0,a-b):
	C=A[i:i+b]
	#print equal(C,B)
	if equal(C,B):
		print i+1,
