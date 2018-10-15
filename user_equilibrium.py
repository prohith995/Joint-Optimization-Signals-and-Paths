import math
from Inputting import *
from delay_function import *

f = open("Converging.txt" , "w+")
g = open("Link_Flows_UE_SS.txt" , "w+")

# Network data
cost = [0]*(m+1)
link = [0]*(m+1)

#Defining the cost of path
def traveltime(j):
	time = t0[j] * (1 + 0.15*math.pow(flow[0][j]*1.0/cap[j],4))
	return time
	
flow = [[0]*(m+1) for i in range(2)] 


# Variables and assigning points to nodes and link no.s to arcs
point = [0]*(n+2)
point[1] = 1
i = 1
for l in range(1,m+1):
	if (tail[l]==(i+1)):
		point[i+1]=l
		i=i+1
point[n+1] = m+1
	

# This function gives the shortest path in each iteration and the flow can be augmented in that path	
def sp(i,j): 
	count = 0
	source = i
	dest = j
	d = [100000]*(n+2)    
	d[source] = 0          
	status = [1]*(n+2) 
	pred = [0]*(n+2)      	         
	prevlink = [0]*(n+2)
	time = [0]*(m+1)	
		
	fcost_path = 0	

	# Function to calcuate the node with minimun temporary distance label
	def mini():

		mininode = 0						
		mind = 1000000
		for i in range(1,n+1):		
			if ( (d[i]<mind) and (status[i]==1) ):
				mind = d[i]
				mininode = i
		return mininode	



	# Step 2 : Selecting a node from set S'
	while(mini()!=dest):
		node = mini()
	
	# Step 3 : Arc Processing
		for l in range( point[node] , point[node+1] ):

			time[l] = traveltime(l) + delay( head[l] , tail[l] , flow[0][l] )

			if( (d[head[l]] > d[node] + time[l]) and (status[head[l]]==1) ):
				d[head[l]] = d[node] + time[l]
				pred[head[l]] = node
				prevlink[head[l]] = l
		status[node] = 0
	node = dest
	time_path = 0
	while (node!=source):
		
		flow[1][prevlink[node]] = flow[1][prevlink[node]] + od[i][j]
		node = pred[node]
	time_path = d[dest]
	return time_path

# These are iterations for the algorithm to converge
# at each iteration, the formula (lambda*new flow + (1-lambda)*old flow ) is used
for Iter in range(1,100):
	
	lamda = 1.0/Iter
			
	flow[1] = [0]*(m+1)
	
	for x in range(1,n+1):
		for y in range(1,n+1):
			
			if (od[x][y]!=0):
				sp(x,y)
				
	for s in range(1,m+1):
		
		flow[0][s] = lamda*flow[1][s] + (1-lamda)*flow[0][s]		
	
	t = 0
	for l in range(1,m+1):
		t = t + flow[0][l]*(traveltime(l) + delay(head[l],tail[l],flow[0][l]))
	f.write(str(t) + "\n")

# prints the equilibrium link flows	
print "The final equilibrium flows are:"
print flow[0]
for l in range(1,m+1):
	g.write(str(flow[0][l])+"\n")

# prints the total system time
t=0
for l in range(1,m+1):
	t = t + flow[0][l]*(traveltime(l) + delay(head[l],tail[l],flow[0][l]))

print t	

f.close()
g.close()
