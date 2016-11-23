import sys
import cv2
import preprocess
import segmentbeautify


# File paths
filepath = "public/img/"
file = sys.argv[1]

print "\n This is the filename: " + filepath + file + "\n"


# Read image
img = cv2.imread(filepath + file, 0)
print img

# Preprocess the image
img = preprocess.binarize(img)
img = preprocess.removeSaltnPepperNoise(img)

# Segment words and lines
words_mapping, word_spacing, line_spacing = segmentbeautify.extractLines(
    img, file)
print word_spacing, line_spacing

# Beautify the text
beautified = segmentbeautify.beautify(
    img, words_mapping, word_spacing, line_spacing, file, filepath)
print "beautified", beautified
