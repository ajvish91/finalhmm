import extractTrainingData
import hmm
import pickle
import numpy as np
from scipy import sparse


# Finds the maximum length in the array matrix
def findMaxLength(arr):
    maxi = 0
    for i in range(len(arr)):
        if maxi < len(arr[i]):
            maxi = len(arr[i])
    return maxi


# Pads zeros to incomplete sequences
def padZeros(arr, maxi):
    for i in range(len(arr)):
        if len(arr[i]) < maxi:
            diff = maxi - len(arr[i])
            for j in range(diff):
                arr[i].append(0)
    return arr


# gets x and y data from the training csv
x_data, y_data = extractTrainingData.getTrainData("main_sequence.csv")


# print (x_data.shape), (y_data.shape), y_data, x_data[0]

# Sample test data
x_test = [[1, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1]]
y_test = np.array(["sugar", "in"])


maxlen = findMaxLength(x_data)
# print maxlen
padded = padZeros(x_data, maxlen)
# print len(padded)

# Convert the data into a sparse matrix
X_data = sparse.csr_matrix(padded)


# Obtain the classifier
clf = hmm.trainHMM(X_data, y_data)

print clf, type(clf)

# dump the classifier
dumpfile = open("classifier", 'w')
pickle.dump(clf, dumpfile)
print "written"
dumpfile.close()


# Reuse the classifier
testfile = open("classifier", 'rb')
test_clf = pickle.load(testfile)
print test_clf, type(test_clf)

X_test = sparse.csr_matrix(padZeros(x_data, findMaxLength(x_data)))

hmm.testHMM(test_clf, X_test, y_test)
