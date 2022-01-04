

from imagedecoder import decode_image
from textfinder import find_words_by_mask
from lettersizefinder import get_letter_size

names = ["szyfr_1", "szyfr_2", "szyfr_3"]

for img_name in names:
    #decode_image(f"Szyfr\\{img_name}.png", img_name)
    pass

masks = [[5, 6, 6, 6, 6, 1, 10], [5, 10, 6, 1, 11, 6, 6, 8, 3, 8, 5], [8, 9, 8, 2, 3, 6]]

for mask in masks:
    words = find_words_by_mask('./Szyfr/w_pustyni_i_w_puszczy.txt', mask)
    print(words)

for img_name in names:
    width, height = get_letter_size(f"decoded-{img_name}.png")
    print(width, height)










