import extractTrainingData
import hmm
import pickle
import numpy as np

x_data, y_data = extractTrainingData.getTrainData("main_sequence.csv")

x_test = np.array([[1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1]])
y_test = np.array(["sugar", "in"])

print (x_data.shape), (y_data.shape), y_data

print x_data
clf = hmm.trainHMM(x_data, y_data)

print clf, type(clf)

dumpfile = open("classifier", 'w')
pickle.dump(clf, dumpfile)
print "written"
dumpfile.close()
testfile = open("classifier", 'rb')
test_clf = pickle.load(testfile)
print test_clf, type(test_clf)

hmm.testHMM(test_clf, x_test, y_test)
