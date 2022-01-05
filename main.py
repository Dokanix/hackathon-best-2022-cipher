

from Letter import Letter
from Line import Line
from Sentence import Sentence
from imagedecoder import decode_image
from textfinder import find_words_by_mask
from lettersizefinder import get_letter_size
import cv2
import numpy as np

img = cv2.imread('decoded-szyfr_1.png')
img = cv2.bitwise_not(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- performing Otsu threshold ---
ret, thresh1 = cv2.threshold(
    gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# --- choosing the right kernel
# --- kernel size of 3 rows (to join dots above letters 'i' and 'j')
# --- and 10 columns to join neighboring letters in words and neighboring words
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# ---Finding contours ---
letterContours, hierarchy = cv2.findContours(
    dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

avg_letter_area = 0

for cnt in letterContours:
    x, y, w, h = cv2.boundingRect(cnt)
    avg_letter_area += w*h

avg_letter_area /= len(letterContours)
unified_countours = []

for cnt in letterContours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w*h > avg_letter_area * 1.7:
        unified_countours.append((x, y, round(w/2), h))
        unified_countours.append(
            (round(x+w/2), y, round(w/2), h))
    elif w*h > avg_letter_area/2:
        unified_countours.append((x, y, w, h))

letters = []
for (x, y, w, h) in unified_countours:
    letters.append(Letter(x, y, w, h))

sentence = Sentence(im2.shape[1])
for letter in letters:
    sentence.place_letter_in_line(letter)

sentence.sort_letters_in_lines()
sentence.sort_lines()
# print(len(sentence.lines))
sentence.split_into_words()
sentence.join_potential_lines()

overall_lengths = []

for line in sentence.lines:
    #print(line.words_lengths(), ' ', line.should_merge)
    overall_lengths.extend(line.words_lengths())

print(overall_lengths)

iter = 0
# for letter in sentence.lines[1].letters:
#     iter += 1
#     cv2.rectangle(im2, (letter.x, letter.y), (letter.x + letter.w, letter.y + letter.h),
#                   (0, 255 * iter/len(sentence.lines[1].letters), 0), 1)


cv2.imwrite('output.png', im2)
