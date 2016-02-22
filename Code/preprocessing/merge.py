from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
from numpy import genfromtxt
import csv
import time

start_time = time.time()
Edges = genfromtxt('../../data/Edges.csv', delimiter=',', skip_header=0, skip_footer=0)
Tuples = genfromtxt('../../data/Tuples.csv', delimiter=',', skip_header=0, skip_footer=0)
print "Size of the Edges (rows, #attributes) ", Edges.shape
print "Size of the Tuples (rows, #attributes) ", Tuples.shape

f = open('../../data/processed_dataset.csv', "w")
f.write('src,dst,ip1,ip2,l12,index_to_time\n')


Matrix = [[0 for x in range(241)] for x in range(240)]

c = 0
for i in range(240):
	for j in range(i+1,241):
		c = c + 1
		Matrix[i][j] = c

with open('../../data/EdgeTuple.csv', 'rb') as csvfile:
    next(csvfile) # To ignore the first line
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        t = row[0]
        e = row[1]
        if (Edges[e,3] > 1):
        	continue
        start = row[2]
        stop = row[3]
        if(int(start) == int(stop)):
        	continue
        c = Matrix[int(start)][int(stop)]
        f.write(str(Tuples[t,1])[:-2]+','+str(Tuples[t,2])[:-2]+',')
        f.write(str(Edges[e,1])[:-2]+','+str(Edges[e,2])[:-2]+','+str(Edges[e,3])[:-2]+','+str(c)+'\n')
print 'Time elapsed %f' % (time.time() - start_time)

