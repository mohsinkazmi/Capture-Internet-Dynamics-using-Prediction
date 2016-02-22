from numpy import *
import matplotlib.pyplot as plt
from kNN import kNN
import time


start_time = time.time()
# Load training and test data
data = genfromtxt('../../data/processed_kNN.csv', delimiter=',', skip_header=1, usecols= (0,5, 10, 11, 12, 13, 14,15,16,17,18,19,21), skip_footer=0)
print "Size of the processed_kNN (rows, #attributes) ", data.shape

# Keep a subset of the training and test data
trainingData = data[:100000,:11]
trainingLabels = data[:,12]

testData = data[100201:100300,:11]
testLabels = data[100201:100300,12]

Matrix = [[0 for x in range(241)] for x in range(240)]

c = 0
for i in range(240):
	for j in range(i+1,241):
		c = c + 1
		Matrix[i][j] = c

arrayIndex_Label = [0,0]
arrayIndex_Predicted = [0,0]
error = [0,0]
def time_startstop(value):
	arrIndex = [0,0]
	for m in range(240):
		for n in range(m+1,241):
			if (Matrix[m][n] == value):
				arrIndex[0] = m
				arrIndex[1] = n
				return arrIndex

# Run kNN algorithm
k = 1
predictedDigits = zeros(testData.shape[0])
digits = zeros(testData.shape[0])
Label_start_stop = zeros((testData.shape[0],2))
Predicted_start_stop = zeros((testData.shape[0],2))
Error_start_stop = zeros((testData.shape[0],2))

for i in range(testData.shape[0]):
    print "Current Test Instance: " + str(i+1)
    print "test data " + str(testData[i]) + "\nLabels " + str(testLabels[i])
    digits[i] = i
    predictedDigits[i] = kNN(k, trainingData, trainingLabels, testData[i,:])
    print "Predicted " + str(predictedDigits[i])
    arrayIndex_Label = time_startstop(testLabels[i])
    Label_start_stop[i,0] = arrayIndex_Label[0]
    Label_start_stop[i,1] = arrayIndex_Label[1]
    arrayIndex_Predicted = time_startstop(predictedDigits[i])
    Predicted_start_stop[i,0] = arrayIndex_Predicted[0]
    Predicted_start_stop[i,1] = arrayIndex_Predicted[1]
    Error_start_stop[i,0] = abs(arrayIndex_Label[0] - arrayIndex_Predicted[0])
    Error_start_stop[i,1] = abs(arrayIndex_Label[1] - arrayIndex_Predicted[1])
    print "start " + str(arrayIndex_Predicted[0]) + " stop " + str(arrayIndex_Predicted[1])
    #print str(i) + " " + str(arrayIndex_Label[0]) + " " + str(arrayIndex_Label[1]) + " " + str(arrayIndex_Predicted[0]) + " " + str(arrayIndex_Predicted[1]) + " " + str(abs(arrayIndex_Label[0] - arrayIndex_Predicted[0])/2.0) + " " + str(abs(arrayIndex_Label[1] - arrayIndex_Predicted[1])/2.0)
    
#plot the Predicted label along with error
f1 = plt.figure()
f2 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.errorbar(digits, Predicted_start_stop[:,0] , yerr=Error_start_stop[:,0], ecolor='g', label="start time error")
ax1.errorbar(digits,Predicted_start_stop[:,1], yerr=Error_start_stop[:,1], ecolor='b', label="stop time error")
ax1.set_xlabel('# of experiments')
ax1.set_ylabel('Predicited label')
ax1.set_title('Predicted label along with error')
plt.draw()

#plot original vs Predicted label
ax2 = f2.add_subplot(111)
ax2.plot(Label_start_stop[:,0], Label_start_stop[:,1],  'b--', label="original label")
ax2.plot(Predicted_start_stop[:,0], Predicted_start_stop[:,1], 'r', label="Predicted label")
ax2.set_xlabel('start time')
ax2.set_ylabel('stop time')
ax2.set_title('original vs Predicted label')
plt.show()
    
# Calculate accuracy
correct = 0

for i in range(testData.shape[0]):
    if predictedDigits[i] == testLabels[i]:
        correct += 1
        
accuracy = correct/float(testData.shape[0])
print
print "K: " + str(k) +" Accuracy: " + str(accuracy)
print 'Time elapsed %f' % (time.time() - start_time)
