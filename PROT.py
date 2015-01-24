import numpy as np
import sys
file = open ("encoding.dat","r")
file2=open ("rosalind_prot.txt","r")
lines2=file2.readlines()
lines=file.readlines()

B=np.zeros(shape=3)
#print lines
def check(A):
	global B
	#print A
        for i in range (0,3):
                if A[i]=='U':
			B[i]=0
		if A[i]=='C':
			B[i]=1
		if A[i]=='A':
			B[i]=2
		if A[i]=='G':
			B[i]=3
	#print B
A=lines2[0]
C=lines[0]
l=len(A)
#A=np.zeros(shape=l-1)
#A=lines2
print A,l
li=[]
for i in xrange (0,l-1,3):
	#print i
	#print A[i:i+3]
	check(A[i:i+3])
	a=B[1]*4+B[2]
	b=B[0]
	#print b
	C=lines[int(a)]
	#print C,int(b)*11+4
	if C[int(b)*11+5]=='t':
		break
	li.append(C[int(b)*11+4])
n=len(li)
for i in range (0,n):
	sys.stdout.write(li[i]),
	
