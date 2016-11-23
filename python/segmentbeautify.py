import cv2
import numpy as np
import conncomp
import math


# Extracts the lines from the images
def extractLines(img, file):
    # Word extraction from machine-# printed area
    word_counter = 0
    # print , len()
    word_array = []

    # Performing Vertical Profile Projection
    vertical = conncomp.verticalProfileProjection(img)
    histogram = vertical["histogram"]
    zero_count = vertical["zero_count"]
    non_zero_count = vertical["non_zero_count"]
    avg_line_spacing = vertical["avg_line_spacing"]
    avg_line_height = vertical["avg_line_height"]

    # Initializing counters
    zero_counter = 0
    non_zero_counter = 0
    i = 0
    total_word_spacing = 0
    total_word_spacing_count = 0

    while ((i < img.shape[0]) and
           (zero_counter < len(zero_count)) and
           (non_zero_counter < len(non_zero_count))):
        # print "Word Counter 1", word_counter
        if histogram[i] == 0:
            i += zero_count[zero_counter]
            zero_counter += 1
        else:
            line = img[i:i + non_zero_count[non_zero_counter],
                       0:img.shape[1] - 1]
            if line.shape[0] < avg_line_height - 30:
                print "Not a line"
            elif avg_line_height * 5 < line.shape[0]:
                horizontal = conncomp.horizontalProfileProjection(line)
                line_avg_word_spacing = horizontal["avg_word_spacing"]
                total_word_spacing += line_avg_word_spacing
                total_word_spacing_count += 1
                this_line = line.shape[0]
                if avg_line_height is None or avg_line_height == 0:
                    avg_line_height = 2
                number_of_lines = int(this_line / avg_line_height)
                print number_of_lines
                sub_lines = np.vsplit(line, number_of_lines)
                for sub_line in sub_lines:
                    inc, new_words = extractWords(sub_line,
                                                  file,
                                                  word_counter)
                    word_counter = inc
                    for word_found in new_words:
                        word_array.append(word_found)
                    # print "Word Counter 3", word_counter, len(word_array)
            else:
                horizontal = conncomp.horizontalProfileProjection(line)
                line_avg_word_spacing = horizontal["avg_word_spacing"]
                total_word_spacing += line_avg_word_spacing
                total_word_spacing_count += 1
                inc, new_words = extractWords(line,
                                              file, word_counter)
                word_counter = inc
                for word_found in new_words:
                    word_array.append(word_found)
                # print "Word Counter 3", word_counter, len(word_array)
            i += non_zero_count[non_zero_counter]
            non_zero_counter += 1
    # print len(word_array)
    return (word_array, (total_word_spacing / total_word_spacing_count),
            avg_line_spacing)


# Extracts the words from the image
def extractWords(img, file, word_counter):
    # Get horizontal profile of the line
    horizontal = conncomp.horizontalProfileProjection(img)
    histogram = horizontal["histogram"]
    zero_count = horizontal["zero_count"]
    non_zero_count = horizontal["non_zero_count"]
    avg_word_spacing = horizontal["avg_word_spacing"]
    avg_word_width = horizontal["avg_word_width"]

    # Initializing the counters
    zero_counter = 0
    non_zero_counter = 0
    i = 0

    # Word Array accumulator
    word_array = []

    # print avg_word_width, avg_word_spacing
    while ((i < img.shape[1]) and
           (zero_counter < len(zero_count)) and
           (non_zero_counter < len(non_zero_count))):
        if histogram[i] == 0:
            if zero_count[zero_counter] < avg_word_spacing - 50:
                i += non_zero_count[non_zero_counter]
                non_zero_counter += 1
            i += zero_count[zero_counter]
            zero_counter += 1
        else:
            word = img[0:img.shape[0] - 1,
                       i:i + non_zero_count[non_zero_counter]]
            if (word.shape[1] < avg_word_width / 2.5 or
                    zero_count[zero_counter - 1] < avg_word_spacing / 2):
                word = np.hstack((img[0:img.shape[0] - 1, i -
                                      zero_count[zero_counter - 1] -
                                      non_zero_count[non_zero_counter - 1]:
                                      i - zero_count[zero_counter - 1]],
                                  word))
                if len(word_array) == 0:
                    word_array.append(word / 255)
                else:
                    word_array[-1] = word / 255
                # print "not a word", [word_counter]
            else:
                word_array.append(word / 255)
                word_counter += 1
            i += non_zero_count[non_zero_counter]
            non_zero_counter += 1
    return word_counter, word_array


# Beautifies the words
def beautify(page, words, word_space, line_space, file, filepath):
    empty_page = np.ones(page.shape) * 255.0
    if(line_space is None or math.isnan(line_space) is True):
        top = 5
    else:
        top = int(line_space * 4)
    if(word_space is None or math.isnan(word_space) is True):
        side = 5
    else:
        side = int(word_space * 5)
    vlocation = int(top)
    hlocation = int(side)
    for word in words:
        word = cv2.resize(word, (word.shape[1] * 90 / word.shape[0], 90))
        print vlocation, hlocation
        empty_page[vlocation:vlocation + word.shape[0],
                   hlocation: hlocation + word.shape[1]] = word * 255.0
        hlocation += word.shape[1] + 10 + word_space
        print word
        if (page.shape[0] - top <= vlocation):
            print "overflow"
            break
        elif (page.shape[1] - word.shape[1] - side <= hlocation):
            vlocation += line_space + word.shape[0]
            hlocation = side
        else:
            continue
    print empty_page
    # back = cv2.cvtColor(empty_page, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(filepath + "/beautified_" + file,
                empty_page)
    # cv2.namedWindow("beauty", cv2.WINDOW_NORMAL)
    # cv2.imshow("beauty", empty_page)
    # cv2.waitKey(10000)
    return empty_page
