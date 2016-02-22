from numpy import *
from euclideanDistance import euclideanDistance

def kNN(k, X, labels, y):
    # Assigns to the test instance the label of the majority of the labels of the k closest 
	# training examples using the kNN with euclidean distance.
    #
    # Input: k: number of nearest neighbors
    #        X: training data           
    #        labels: class labels of training data
    #        y: test data

    # Instructions: Run the kNN algorithm to predict the class of
    #               y. Rows of X correspond to observations, columns
    #               to features. The 'labels' vector contains the 
    #               class to which each observation of the training 
    #               data X belongs. Calculate the distance betweet y and each 
    #               row of X, find  the k closest observations and give y 
    #               the class of the majority of them.
    #
    # Note: To compute the distance betweet two vectors A and B use
    #       use the euclideanDistance(A,B) function.
    #

	row = X.shape[0]
	col = X.shape[1]
	dis = zeros(row)
	for i in range(row):
		dis[i] = euclideanDistance(X[i,:],y)

	index = dis.argsort()

	labels = labels[index]

	count = zeros(max(labels)+1)
	for j in range(k):
		count[labels[j]] += 1
	
	label = argmax(count)
	argmax(dis)
    return label

 
