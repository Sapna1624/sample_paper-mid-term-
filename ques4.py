import math
D=list(map(int,input().split(",")))
C=50
H=30
for i in D:
	s=int(math.sqrt((2*C*i)/H))
	print(s,end=",")
