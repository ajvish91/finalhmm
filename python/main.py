import sys
import cv2
import preprocess
import segmentbeautify


filepath = "public/img/"
file = sys.argv[1]

print "\n This is the filename: " + filepath + file + "\n"

img = cv2.imread(filepath + file, 0)
print img
img = preprocess.binarize(img)
img = preprocess.removeSaltnPepperNoise(img)
words_mapping, word_spacing, line_spacing = segmentbeautify.extractLines(
    img, file)
print word_spacing, line_spacing
beautified = segmentbeautify.beautify(
    img, words_mapping, word_spacing, line_spacing, file, filepath)
print "beautified", beautified
