from numpy import *
import pylab
from numpy import genfromtxt
import csv
import time
import socket, struct

start_time = time.time()

f = open('../../data/processed_dataset_2.csv', "w")
f.write('ip-id,ip,as,long,lati,att\n')

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

with open('../../data/Ips.csv', 'rb') as csvfile:
    next(csvfile) # To ignore the first line
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
		print row[1]
		try:
			c = ip2long(row[1])
		
		except:
			continue
		f.write(str(row[0])+','+str(c)+',')
		f.write(str(row[2])+','+str(row[3])+','+str(row[4])+','+str(row[13])+'\n')
print 'Time elapsed %f' % (time.time() - start_time)



