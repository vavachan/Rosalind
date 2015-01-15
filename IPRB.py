k=input()
m=input()
n=input()
tot=m+n+k
PhomD=k*1.0/tot
Phet=m*1.0/tot
PhomR=n*1.0/tot
Prob=PhomD
Prob=Prob+PhomD*m/(tot-1)
Prob=Prob+PhomD*n/(tot-1)
Prob=Prob+Phet*(m-1)/(tot-1)*.75
Prob=Prob+Phet*(n)/(tot-1)*.5
Prob=Prob+PhomR*m/(tot-1)*.5
print Prob






