from numpy import *
import matplotlib.pyplot as plt
from matplotlib.mlab import PCA
from mpl_toolkits.mplot3d import Axes3D
import pylab
from numpy import genfromtxt

my_data = genfromtxt('../../data/small_dataset_all.csv', delimiter=',', skip_header=1, usecols= (0, 1,4,5,6,7,8), skip_footer=0)
results = PCA(my_data)

x = []
y = []
z = []
for item in results.Y:
	x.append(item[0])
	y.append(item[1])
	z.append(item[2])
	m.append(item[3])
 

plt.close('all') # close all latent plotting windows
fig1 = plt.figure() # Make a plotting figure
ax = Axes3D(fig1) # use the plotting figure to create a Axis3D object.
pltData = [x,y,z] 
ax.scatter(pltData[0], pltData[1], pltData[2])


# label the axes 
ax.set_xlabel("x-axis label") 
ax.set_ylabel("y-axis label")
ax.set_zlabel("z-axis label")
ax.set_title("The title of the plot")
#fig1.savefig('PCA.png')
plt.show() # show the plot
