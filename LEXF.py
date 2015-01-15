import numpy as np
import sys
file=open("rosalind_lexf.txt","r")
lines=file.readline()
p=input()
n=len(lines)-1
print lines,n
A=np.zeros(shape=n)
A=lines
print A
B=np.zeros(shape=p)
for i in range (0,p):
	B[i]=1
def nested_loop(POS):
	global A,B,p
	if POS>=p:
		return
	i=0
	while 1: 
		nested_loop(POS+1)
		if i>=n-1:
			break
		B[POS]=B[POS]+1
		for k in range (0,p):
	#		print B[k],
			sys.stdout.write(A[int(B[k])-1]),
		print ''
		i=i+1
		
	B[POS]=1
		
	
for k in range (0,p):
#	print B[k],
	sys.stdout.write(A[int(B[k])-1]),
print ''
nested_loop(0)
