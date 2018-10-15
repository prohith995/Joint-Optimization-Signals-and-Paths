import math
from Inputting import *

ct = 120
gt = [[1]*(n+1) for i in range(n+1)]

gt[3][4] = 0.69
gt[5][4] = 0.69
gt[11][4] = 0.31
gt[4][5] = 0.71
gt[6][5] = 0.71
gt[9][5] = 0.29
gt[2][6] = 0.77
gt[5][6] = 0.28
gt[8][6] = 0.77
gt[6][8] = 0.6
gt[7][8] = 0.4
gt[9][8] = 0.4
gt[16][8] = 0.6
gt[5][9] = 0.56
gt[8][9] = 0.44
gt[10][9] = 0.56
gt[9][10] = .64
gt[11][10] = 0.36
gt[16][10] = 0.36
#gt[25][10] = 0.64
gt[4][11] = 0.52
gt[10][11] = 0.48
gt[12][11] = 0.48
gt[14][11] = 0.52
gt[11][14] = 0.73
gt[15][14] = 0.27
gt[23][14] = 0.73
gt[14][15] = 0.44
gt[19][15] = 0.44
gt[22][15] = 0.56
#gt[25][15] = 0.56
gt[8][16] = 0.23
gt[10][16] = 0.77
gt[17][16] = 0.23
gt[18][16] = 0.77
gt[10][17] = 0.38
gt[16][17] = 0.62
gt[19][17] = 0.62
gt[15][19] = 0.28
gt[17][19] = 0.72
gt[20][19] = 0.72


def link(i,j):
	for l in range(m+1):
		if ((head[l]==j) & (tail[l]==i)):
			return l

def delay(i,j,flow):

	l = link(i,j)
	d1 = ct*math.pow( 1-gt[i][j] , 2)
	d2 = 2*(1-flow*1.0*gt[i][j]/cap[l])
	
	if (gt[i][j] == 1) : d = 0
	else: d = 0.9 * d1*1.0/d2	
	
	return d

def mardelay(i,j,flow):
	
	l = link(i,j)
	d1 = ct*math.pow( 1-gt[i][j] , 2)
	d2 = 2*(1-flow*1.0*gt[i][j]/cap[l])

	dd2 = d1*2.0*gt[i][j]/(cap[l]*d2*d2)

	if (gt[i][j] == 1) : d = 0
	else: d = 0.9*(flow*1.0*dd2 + d1*1.0/d2)

	return d
	
