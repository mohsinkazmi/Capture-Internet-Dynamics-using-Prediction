from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
from numpy import genfromtxt
import csv
import time

start_time = time.time()
IP = genfromtxt('../../data/processed_dataset_2.csv', delimiter=',', skip_header=1, skip_footer=0) #ip-id,ip,as,long,lati,att
print "Size of the processed_dataset_2 (rows, #attributes) ", IP.shape

f = open('../../data/processed_kNN.csv', "w")
f.write('ip,as,long,lati,att,ip,as,long,lati,att,id,ip,as,long,lati,att,id,ip,as,long,lati,att,id,l12,index_to_time\n')


with open('../../data/processed_dataset.csv', 'rb') as csvfile: # src,dst,ip1,ip2,l12,index_to_time
    next(csvfile) # To ignore the first line
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
    	src = row[0]
    	dst = row[1]
    	ip1 = row[2]
    	ip2 = row[3]
    	l12 = row[4]
    	index_to_time = row[5]
    	i = -1
    	j = -1
    	k = -1
    	l = -1
    	for a in range(IP.shape[0]):
    		if (str(IP[a,0])[:-2] == src):
    			i = a
    			break
    	for b in range(IP.shape[0]):
    		if (str(IP[b,0])[:-2] == dst):
    			j = b
    			break
    	for c in range(IP.shape[0]):
    		if (str(IP[c,0])[:-2] == ip1):
    			k = c
    			break
    	for d in range(IP.shape[0]):
    		if (str(IP[d,0])[:-2] == ip2):
    			l = d
    			break
    		
    	if (i == -1 or j == -1 or k == -1 or l == -1):
    		continue
    	f.write(str(IP[i,1])[:-2]+','+str(IP[i,2])[:-2]+','+str(IP[i,3])[:-2]+','+str(IP[i,4])[:-2]+','+str(IP[i,5])[:-2]+',')
    	f.write(str(IP[j,1])[:-2]+','+str(IP[j,2])[:-2]+','+str(IP[j,3])[:-2]+','+str(IP[j,4])[:-2]+','+str(IP[j,5])[:-2]+',')
    	f.write(str(IP[k,1])[:-2]+','+str(IP[k,2])[:-2]+','+str(IP[k,3])[:-2]+','+str(IP[k,4])[:-2]+','+str(IP[k,5])[:-2]+',')
    	f.write(str(IP[l,1])[:-2]+','+str(IP[l,2])[:-2]+','+str(IP[l,3])[:-2]+','+str(IP[l,4])[:-2]+','+str(IP[l,5])[:-2]+',')
    	f.write(str(l12)+','+str(index_to_time)+'\n')
print 'Time elapsed %f' % (time.time() - start_time)
