from seqlearn.hmm import MultinomialHMM
from seqlearn.evaluation import whole_sequence_accuracy
import numpy as np


# Gets the features from test.txt
def features(sequence, i):
    split_sequence = sequence[i].split(" ")
    # print sequence[i], i
    for ele in (split_sequence):
        yield ele
    # yield sequence[i]


def createTXT(words):
    # Saves the image into a TXT file
    for word in words:
        f_handle = file('test.txt', 'a')
        np.savetxt(f_handle, word[0].flatten(), delimiter=" ",
                   fmt="%i", newline=" ",
                   header='', footer="" + word[1] + "\n\n",
                   comments='')
        f_handle.close()
    return "test.txt"


def trainHMM(X_train, y_train):
    # # # Extracts features from the datasets
    # X_train, y_train, lengths_train = load_conll(data, features)
    # # Models it as an HMM
    clf = MultinomialHMM()
    print "y shape", y_train.shape[0]
    lengths_train = []
    for x in X_train:
        lengths_train.append(0)

    print lengths_train
    clf.fit(X_train, y_train, [y_train.shape[0]])

    # print X_train, y_train
    return clf


def testHMM(clf, X_test, y_test):

    # Validation after training
    y_pred = clf.predict(X_test, [X_test.shape[0]])

    print y_pred
    # # Final score
    print(whole_sequence_accuracy(y_test, y_pred, [X_test.shape[0]]))


def predictHMM(clf, X_predict):
    # Validation after training
    y_pred = clf.predict(X_predict, 1)

    print y_pred
    # # # Final score
    # print(whole_sequence_accuracy(y_test, y_pred, lengths_test))
