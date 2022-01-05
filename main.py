

from imagedecoder import decode_image
from textfinder import find_words_by_mask
from lettersizefinder import get_letter_size
import cv2
import numpy as np

img = cv2.imread('decoded-szyfr_3.png')
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
letterCountorus, hierarchy = cv2.findContours(
    dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

avg_letter_area = 0

for cnt in letterCountorus:
    x, y, w, h = cv2.boundingRect(cnt)
    avg_letter_area += w*h

avg_letter_area /= len(letterCountorus)
unified_countours = []

iter = 0
for cnt in letterCountorus:
    iter += 1
    x, y, w, h = cv2.boundingRect(cnt)
    if w*h > avg_letter_area * 1.7:
        unified_countours.append((x, y, round(w/2), h))
        unified_countours.append(
            (round(x+w/2), y, round(w/2), h))
    elif w*h > avg_letter_area/2:
        unified_countours.append((x, y, w, h))


for (x, y, w, h) in unified_countours:
    cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 1)


cv2.imwrite('output.png', im2)
