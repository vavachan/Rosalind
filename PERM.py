import numpy as np

n=input()
A=np.zeros(shape=(n))
B=np.zeros(shape=(n,n))
for i in range (0,n):
	A[i]=i+1
i=0
count=n-1
k=0
def nestedloop():
	global count,k
	global A
	k=k+1
	l=k-1
	i=count
	nc=count
	#print B
	if count==0:
		print A
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

nestedloop()
