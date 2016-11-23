import sys
import numpy as np
import csv
maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt / 10)
        decrement = True


def getTrainData(filepath):
    # add path of the file
    with open(filepath, 'r') as dest_f:
        data_iter = csv.reader(dest_f,
                               delimiter=',')
        data = [data for data in data_iter]
    # change number of training and testing data
    numTrainData = 11
    numTestData = 2

    np.random.shuffle(data)

    print "Wrote the data"
    train_data = data[0:numTrainData]
    writeToFile(train_data, "train.txt")
    print len(train_data)
    x_train = []
    y_train = []
    for i in range(len(train_data)):
        x_train.append(train_data[i][:-2])
        y_train.append(train_data[i][-1])

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    test_data = data[numTrainData + 1: numTrainData + numTestData]
    writeToFile(test_data, "test.txt")
    # x_test = test_data[: -2]
    # y_test = test_data[-1:]
    # can return x_test, y_test also
    return x_train, y_train


def writeToFile(data, fileName):
    textfile = open(fileName, 'w')
    for item in data:
        textfile.write("%s\n" % item)
    return
