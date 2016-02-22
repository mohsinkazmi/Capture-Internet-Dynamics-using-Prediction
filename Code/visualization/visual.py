from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
from numpy import genfromtxt

my_data = genfromtxt('../../data/Ips.csv', delimiter=',', skip_header=0, usecols= (0,1, 2, 3, 4, 13, 14), skip_footer=0) #ip_id, ip, as, long., lati, att, id
data = my_data[:,1:]
target= my_data[:,0]
print "Size of the data (rows, #attributes) ", my_data.shape

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
ax1.scatter(my_data[:,2],my_data[:,6],my_data[:,5] ,c=target)
ax1.set_xlabel('1st dimension (AS)')
ax1.set_ylabel('2nd dimension (id)')
ax1.set_zlabel('3rd dimension (att)')
ax1.set_title("Vizualization of the dataset (3 out of 6 dimensions)")
plt.draw()

plt.figure(2)
plt.scatter(my_data[:,3],my_data[:,4], c=target)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title("Vizualization of the dataset w.r.t Geolocation")
plt.draw()

plt.figure(3)
plt.scatter(my_data[:,0],my_data[:,2], c=target)
plt.xlabel('IP')
plt.ylabel('AS')
plt.title("Vizualization of the dataset w.r.t AS")
plt.show()
