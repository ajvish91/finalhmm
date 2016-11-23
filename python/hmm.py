from seqlearn.hmm import MultinomialHMM
from seqlearn.evaluation import whole_sequence_accuracy
import numpy as np


# Gets the features from test.txt
def features(sequence, i):
    split_sequence = sequence[i].split(" ")
    for ele in (split_sequence):
        yield ele


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
    # # Models it as an HMM
    clf = MultinomialHMM()
    print "y shape", y_train.shape[0]
    lengths_train = []
    for x in X_train:
        lengths_train.append(0)

    print lengths_train
    clf.fit(X_train, y_train, [len(y_train)])

    return clf


def testHMM(clf, X_test, y_test):

    # Validation after training
    y_pred = clf.predict(X_test, [len(y_test)])

    print y_pred
    # # Final score
    print(whole_sequence_accuracy(y_test, y_pred, [len(y_test)]))


def predictHMM(clf, X_predict):
    # Validation after training
    y_pred = clf.predict(X_predict, 1)

    print y_pred
