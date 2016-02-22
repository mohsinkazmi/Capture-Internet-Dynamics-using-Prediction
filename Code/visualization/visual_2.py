from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
from numpy import genfromtxt
from numpy import subtract
import csv


my_data = genfromtxt('../../data/dataset_all_new.csv', delimiter=',', skip_header=1, usecols= (0, 1), skip_footer=0)
my_data2 = genfromtxt('data/dataset_all_new.csv', delimiter=',', skip_header=1, usecols= (7, 8), skip_footer=0)

print "Size of the data (rows, #attributes) ", my_data.shape
print "Size of the data (rows, #attributes) ", my_data2.shape

time = subtract(my_data2[:,1], my_data2[:,0])

plt.figure(1)
plt.scatter(my_data[:100000,0],my_data[:100000,1], c=time[:100000])
plt.xlabel('1st dimension (src)')
plt.ylabel('2nd dimension (dst)')
plt.title("Vizualization of the dataset w.r.t time difference")
plt.draw()

plt.figure(2)
plt.scatter(my_data2[:100000,0], my_data2[:100000,1], c=time[:100000])
plt.xlabel('start time')
plt.ylabel('stop time')
plt.title("Vizualization of the dataset w.r.t time difference")
plt.show()
