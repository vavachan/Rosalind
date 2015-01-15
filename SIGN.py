import numpy as np
percount=0
print 'Enter n:'
n=input()
A=np.zeros(shape=(n))
B=np.zeros(shape=(n,n))
C=np.zeros(shape=(n))
for i in range (0,n):
	A[i]=i+1
i=0
count=n-1
k=0
def sign():
	global A
	C=np.copy(A)
	for k in range (0,n):
		print int(C[k]),
	print ''
	for p in range (0,n):
		A=np.copy(C)
		#print A,C,p
		for k in range (0,n):
			if k==p:
				print int(-A[k]),
			else:
				print int(A[k]),
		print ''	
		for i in range (p,n-1):
			for j in range (1,n):
				#print i+j
				if i+j>=n:
				#	print i+j
					break
				for k in range (0,n):
					if k==i+j or k==i:
						print int(-A[k]),
					else :
						print int(A[k]),
				print ''
			A[i]=-A[i]
def nestedloop():
	global count,k,percount
	global A
	k=k+1
	l=k-1
	i=count
	nc=count
	#print B
	if count==0:
		percount=percount+1
		sign()
	while i >= 0 :
		temp=A[i]
		A[i]=A[nc]
		A[nc]=temp
	
		count=count-1
		for j in range (0,n):
			B[l][j]=A[j]
		nestedloop()
		for j in range (0,n):
			A[j]=B[l][j]
		count=nc
		temp=A[nc]
		A[nc]=A[i]
		A[i]=temp
		i=i-1
	k=k-1
print 'The permutations are :'
nestedloop()
print 'The number permutations are:'
print percount*2**n
