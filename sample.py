import math

def fincost(j,succ):
	i = link[j]
	cost = fcost[i] + vpar[i]*math.pow(flow[i],vexp[i]) + sig_new[j][succ]*delay[i]
	return cost
n=5
m=6

delay = [0,3,3,3,3,3,3]
cost = [0,0,0,0,0,0,0]
tail = [0,3,1,2,3,1,5]
head = [0,5,3,4,4,2,4]
fcost = [0,3,5,4,6,7,4]
vpar = [0,5,3,6,3,2,3]
vexp = [0,2,2,2,2,3,2]
link = [0,0,0,0,0,0,0]
flow = [2,3,4,2,3,4,3]
point = [0,0,0,0,0,0,0]

sign = [[0]*(m+1) for i in range(m+1)]
sign[2][4] = 1
sign[1][6] = 1
sig_new = [[0]*(m+1) for i in range(m+1)]


s = [0,0,0,0,0,0,0]
k=1


point[1] = 1
for i in range(1,n+1):
	minhead = 99
	z = 1
	while(z!=0):

		print i,minhead
		minhead = 100
		jop = 0		
		z = 0
		for j in range(1,m+1):
			
			if (tail[j]==i)&(s[j]==0):
				z = z+1
				if (head[j] < minhead) :
					print minhead,head[j]
					minhead = head[j]
					jop = j
			
		if (z!=0):
	
			link[k] = jop
			s[jop] = 1
			k = k+1
	point[i+1] = k		
	
print link
#print fincost
for i in range(1,m+1):
	for j in range(1,m+1):
		sig_new[link[i]][link[j]] = sign[i][j]


for i in range(1,m+1):
	print fincost(i,0)

print point
