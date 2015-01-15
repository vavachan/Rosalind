import numpy as np
import sys
file=open("rosalind_lexv.txt","r")
n=input()
lines=file.readlines()
B=np.zeros(shape=n)
A=lines[0]
p=len(A)
def Nest(POS):
	global A,B
	if POS>=n:
		return
	for i in range (0,p-1): 
		B[POS]=B[POS]+1
		for k in range (0,n):
         	      #print B[k],
			if B[k]==0:
				sys.stdout.write(''),
			else :
               	        	sys.stdout.write(A[int(B[k])-1]),
                print ''

		Nest(POS+1)
	B[POS]=0
Nest(0)
