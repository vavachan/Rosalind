file=open("rosalind_gc.txt","r")
lines = file.readlines()
percentage=0
lab_per=0
while 1:
	i=0
	a=lines[i]
	if a[0]=='>' :
		i=i+1
		if percentage >= lab_per:
			label=a
			lab_per=percentage
		percentage=0
	a=lines[i]
	GCcont=0
	print a 
	k=0
	while 1:
		if k==len(a) :
			percentage=GCcont/len(a)*100
			break
		if a[k]=='G' or a[k] == 'C' :
			GCcont=GCcont+1	
		print len(a),k,i
		k=k+1
	print 'helo'
	i=i+1
print label
print lab_per
	
